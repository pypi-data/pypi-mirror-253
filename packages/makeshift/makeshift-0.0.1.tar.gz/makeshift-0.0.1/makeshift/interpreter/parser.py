"""The parser takes the list of Tokens from the Lexer and builds an 
abstract syntax tree.

"""

from makeshift.interpreter.utils import GeneratorSyntaxError
from makeshift.interpreter.token import Token, TokenType
from makeshift.interpreter import ast

class Parser():
	def __init__(self, tokens):
		self.tokens = tokens
		self.pos = 0 #points to the next token to be read

	def consume(self):
		#return the next token and move the pointer
		#up one
		if not self.is_at_end():
			self.pos += 1
			return(self.previous())

	def peek(self, ct = 0):
		#look at the next token without consuming
		return(self.tokens[self.pos + ct])

	def check(self, token_type):
		#Check if the next token is the type we need
		return(self.peek().type == token_type)

	def match(self, token_types):
		return(self.peek().type in token_types)

	def expect(self, token_type):
		#like Check, but with error-throwing teeth
		if not self.check(token_type):
			raise GeneratorSyntaxError(f'Expected {token_type} in line'\
				f' {self.peek().line} pos {self.peek().offset} but got'\
				f' {self.peek().type}')

	def is_at_end(self):
		#check if the next token is the end of the file
		return(self.check(TokenType.EOF))

	def previous(self):
		return(self.tokens[self.pos - 1])

	def generator(self, title):
		def_list = []
		while not self.is_at_end():
			def_list.append(self.definition())

		return(ast.Generator(title = 'test.txt', definitions = def_list, 
			top_definition = def_list[0]))

	def definition(self):
		name = self.name()
		if self.check(TokenType.NEWLINE):
			self.consume()
		else:
			raise GeneratorSyntaxError(f'expected newline after name in '\
				f'line {self.peek().line} but got {self.peek().type}')
		
		options = []
		while self.check(TokenType.TAB):
			self.consume()
			if self.check(TokenType.NEWLINE):
				self.consume()
				continue
			options.append(self.option())
		return(ast.Definition(name = name, options = options))

	def name(self):
		if not self.check(TokenType.STRING):
			raise GeneratorSyntaxError(f'Expected string for name definition'\
				f' in line {self.peek().line} but got {self.peek().type}')

		return(ast.Name(self.consume().value.strip()))

	def option(self):
		#TO DO figure out how to parse out the percentage
		#for now we'll just parse all the expressions

		#we'll rely on Expression to know when to stop and save
		#the Percent portion for the option
		expression = self.expression()
		if self.check(TokenType.NEWLINE) or self.check(TokenType.EOF):
			if self.check(TokenType.NEWLINE):
				self.consume()
			return(ast.Option(expression = expression))

		elif self.check(TokenType.NUMBER):
			number = int(self.consume().value)
			if self.check(TokenType.PERCENT):
				self.consume()
			else:
				raise GeneratorSyntaxError(f'Expected % after number at end of option'\
					 f'in line {self.peek().line} but got {self.peek().type}')
			if self.check(TokenType.NEWLINE):
				self.consume()
			else:
				raise GeneratorSyntaxError(f'Expected NEWLINE at end of option'\
					 f'in line {self.peek().line} but got {self.peek().type}')

			last = expression.subexpressions[-1]
			if isinstance(last, ast.String_Literal):
				last.value = last.value.rstrip() #peel off whitepsace between string and percent

			return(ast.Option(expression = expression, percent = number))

	def expression(self):
		subexpressions = []
		while self.match({TokenType.STRING, TokenType.OPEN_BRACE, TokenType.NUMBER}):
			if self.check(TokenType.STRING):
				subexpressions.append(self.string_literal())
			elif self.check(TokenType.OPEN_BRACE):
				self.consume()
				subexpressions.append(self.resolvable())
				self.expect(TokenType.CLOSE_BRACE)
				self.consume()
			elif self.check(TokenType.NUMBER):
				if self.peek(1).type != TokenType.PERCENT:
					subexpressions.append(self.string_literal())
				else:
					break
		return(ast.Expression(subexpressions))

	def resolvable(self):
		segments = []
		while self.match({TokenType.STRING, TokenType.BAR, TokenType.OPEN_BRACE}):
			if self.check(TokenType.STRING):
				if not ' ' in self.peek().value.strip():
					segments.append(self.reference())
				else:
					segments.append(self.expression())
			elif self.check(TokenType.BAR):
				self.consume()
				#segments.append(self.resolvable())
			elif self.check(TokenType.OPEN_BRACE):
				segments.append(self.expression())

		return(ast.Resolvable(segments))

	def reference(self):
		name = self.name()
		if self.check(TokenType.DOT):
			self.consume()
			method = self.method()
		else:
			method = None
		return(ast.Reference(name = name, method = method))

	def string_literal(self):
		if self.check(TokenType.NUMBER):
			return(ast.String_Literal(self.consume().value))
		
		string = ''
		while self.check(TokenType.STRING):
			string = string + self.consume().value
		return(ast.String_Literal(string))

	def method(self):
		if not self.check(TokenType.STRING):
			raise GeneratorSyntaxError(f'Expected string for method name'\
				f'in line {self.peek().line} but got {self.peek().type}')

		return(ast.Method(self.consume().value.strip()))