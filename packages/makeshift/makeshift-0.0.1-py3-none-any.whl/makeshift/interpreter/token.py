
from enum import Enum

TokenType = Enum('TokenType', [
	#Paired tokens
	'OPEN_BRACE', 'CLOSE_BRACE',
	'OPEN_PARENTHESIS', 'CLOSE_PARENTHESIS',
	
	#Single-character tokens
	'COLON', 'BAR', 'PERCENT', 'DOT',
	'EQUALS', 'SLASH',

	#Syntactic whitespace tokens
	'TAB', 'NEWLINE',

	#Literals
	'STRING', 'NUMBER', 'IDENTIFIER',

	'EOF'
	])

class Token():
	def __init__(self, tokentype, lexeme, line, offset):
		self.type = tokentype
		self.lexeme = lexeme
		self.line = line
		self.offset = offset

	def __repr__(self):
		if self.type == TokenType.NEWLINE:
			lexeme = '\\n'
		elif self.type == TokenType.TAB:
			lexeme = '\\t'
		else:
			lexeme = self.lexeme
		return(f'Token({self.type}, "{lexeme}", line {self.line}, offset {self.offset})')

	def __eq__(self, other):
		if self.type != other.type:
			return(False)
		if self.lexeme != other.lexeme:
			return(False)
		if self.line != other.line:
			return(False)
		if self.offset != other.offset:
			return(False)
		return(True)

	@property
	def value(self):
		return(self.lexeme)