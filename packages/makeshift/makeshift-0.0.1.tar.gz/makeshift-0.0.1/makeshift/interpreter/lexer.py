# The lexer turns the raw input into a series of defined Tokens

from makeshift.interpreter.utils import GeneratorSyntaxError
from makeshift.interpreter.token import TokenType, Token

KEYS = {
	'OPEN_BRACE': '{',
	'CLOSE_BRACE': '}',
	'COLON': ':',
	'OPEN_BRACKET': '[',
	'CLOSE_BRACKET': ']',
	'OPEN_PARENTHESIS': '(',
	'CLOSE_PARENTHESIS': ')',
	'BAR': '|',
	'DOT': '.',
	'NEWLINE': '\n',
	'TAB': '\t',
	'PERCENT': '%',
	'SLASH': '/',
	'EQUALS': '='
	}

class Lexer():
	def __init__(self, inp):
		self.inp = inp.strip() #leading/trailing whitespace in file doesn't affect the grammar
		self.index = 0
		self.line = 1
		self.offset = 0
		self.tokens = []

	def add_token(self, token_type, literal = None, line = None, offset = None):
		if offset is None:
			offset = self.offset
		if line is None:
			line = self.line
		if token_type.name in KEYS and literal is None:
			literal = KEYS.get(token_type.name)
		self.tokens.append(Token(token_type, literal, line, offset))
		return

	def advance(self):
		self.index += 1
		self.offset += 1
		return(self.inp[self.index - 1])

	def is_at_end(self):
		return(self.index >= len(self.inp))

	def match(self, expected):
		if self.is_at_end():
			return(False)
		elif self.inp[self.index] != expected:
			return(False)

		self.index += 1
		self.offset += 1
		return(True)

	def peek(self):
		if self.is_at_end():
			return(False)
		return(self.inp[self.index])

	def handle_number(self):
		start = self.index - 1

		while not self.is_at_end() and self.peek().isdigit():
			self.advance()

		offset = self.offset - (self.index - start)

		self.add_token(TokenType.NUMBER, self.inp[start:self.index], offset = offset)
		return

	def handle_string(self):
		start = self.index - 1
		
		while (not self.is_at_end()) and (self.peek().isalpha() or self.peek() in {'_', ' ', '\t', '\''}):
			self.advance()

		offset = self.offset - (self.index - start)

		self.add_token(TokenType.STRING, self.inp[start:self.index], offset = offset)
		return

	def lexv2(self):
		while not self.is_at_end():
			start = self.index

			char = self.advance()

			if char == '{':
				self.add_token(TokenType.OPEN_BRACE)
			elif char == '}':
				self.add_token(TokenType.CLOSE_BRACE)
			elif char == '|':
				self.add_token(TokenType.BAR)
			elif char == '.':
				self.add_token(TokenType.DOT)
			elif char == '\t':
				self.add_token(TokenType.TAB)
			elif char == '%':
				self.add_token(TokenType.PERCENT)

			elif char == '/' and self.match('/'):
				while self.peek() != '\n' and not self.is_at_end():
					self.advance()

			elif char == '\n':
				self.add_token(TokenType.NEWLINE)
				self.line += 1
				self.offset = 0
				while self.peek() == '\n' and not self.is_at_end():
					self.advance()
					self.line += 1
					self.offset = 0

			elif char.isdigit():
				self.handle_number()

			elif char.isascii():
				self.handle_string()

			else:
				raise GeneratorSyntaxError(f'Unknown character at line {self.line} position {self.offset}')

		self.add_token(TokenType.EOF, offset = self.offset + 1)

		return(self.tokens)

	def __iter__(self):
		return(self)

	def __next__(self):
		pass