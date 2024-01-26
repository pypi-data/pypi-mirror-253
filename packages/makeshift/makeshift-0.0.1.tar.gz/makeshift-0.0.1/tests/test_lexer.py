

import unittest

#import proclang
from proclang.interpreter.lexer import Lexer
from proclang.interpreter.token import Token, TokenType

class TestLexerMethods(unittest.TestCase):
	#passing empty file
	#normal looking file
	def setUp(self):
		self.lexer = Lexer('abc\n\t123')

	def test_advance(self):
		# x = proclang.lexer.Lexer('abc\n\t123')
		x = self.lexer
		self.assertEqual(x.index, 0)
		self.assertEqual(x.offset, 0)
		self.assertEqual(x.advance(), 'a')
		self.assertEqual(x.index, 1)
		self.assertEqual(x.offset, 1)
		self.assertEqual(x.advance(), 'b')
		self.assertEqual(x.index, 2)
		self.assertEqual(x.offset, 2)
		self.assertEqual(x.advance(), 'c')
		self.assertEqual(x.index, 3)
		self.assertEqual(x.offset, 3)
		self.assertEqual(x.advance(), '\n')
		self.assertEqual(x.index, 4)
		self.assertEqual(x.offset, 4)
		self.assertEqual(x.advance(), '\t')
		self.assertEqual(x.index, 5)
		self.assertEqual(x.offset, 5)
		self.assertEqual(x.advance(), '1')
		self.assertEqual(x.index, 6)
		self.assertEqual(x.offset, 6)
		self.assertEqual(x.advance(), '2')
		self.assertEqual(x.advance(), '3')

	def test_is_at_end(self):
		x = self.lexer
		x.inp = 'a'
		self.assertFalse(x.is_at_end())
		x.advance()
		self.assertTrue(x.is_at_end())

	def test_match(self):
		x = self.lexer
		self.assertTrue(x.match('a'))
		self.assertTrue(x.match('b'))
		self.assertFalse(x.match('\n'))
		self.assertTrue(x.match('c'))
		self.assertTrue(x.match('\n'))
		self.assertTrue(x.match('\t'))
		self.assertTrue(x.match('1'))
		self.assertTrue(x.match('2'))
		self.assertTrue(x.match('3'))
		self.assertFalse(x.match('4'))

	def test_peek(self):
		x = self.lexer
		x.inp = 'abc\n\t1'
		self.assertEqual(x.peek(), 'a')
		x.advance()
		self.assertEqual(x.peek(), 'b')
		x.advance()
		self.assertEqual(x.peek(), 'c')
		x.advance()
		self.assertEqual(x.peek(), '\n')
		x.advance()
		self.assertEqual(x.peek(), '\t')
		x.advance()
		self.assertEqual(x.peek(), '1')
		x.advance()
		self.assertFalse(x.peek())

	def test_add_token(self):
		#TO DO: should check that string requires literal
		x = Lexer('abc\n\t123')
		x.add_token(TokenType.STRING, 'abc', 1, 0)
		x.offset = 3
		#TO DO: should check that newline has no literal(?)
		x.add_token(TokenType.NEWLINE)
		x.offset = 0
		x.line += 1
		x.add_token(TokenType.TAB)
		self.assertEqual(x.tokens,
			[Token(TokenType.STRING, 'abc', 1, 0),
			Token(TokenType.NEWLINE, '\n', line = 1, offset = 3),
			Token(TokenType.TAB, '\t', 2, 0)])

	def test_handle_number(self):
		x = Lexer('999a123')
		x.advance()
		x.handle_number()
		self.assertEqual(x.tokens,
			[Token(TokenType.NUMBER, '999', 1, 0)])

	def test_handle_string(self):
		x = Lexer('abc123')
		x.advance()
		x.handle_string()
		self.assertEqual(x.tokens,
			[Token(TokenType.STRING, 'abc', 1, 0)])
		x = Lexer('abc_ 	\t\'\'__ &3')
		x.advance()
		x.handle_string()
		self.assertEqual(x.tokens,
			[Token(TokenType.STRING, 'abc_ 	\t\'\'__ ', 1, 0)])


class TestLexer(unittest.TestCase):
	
	def test_empty(self):
		#An empty file just returns an EOF
		#[Token(EOF, None, line 1 pos 1)]
		result = Token(TokenType.EOF, None, 1, 1)
		x = Lexer('')
		self.assertEqual(x.lexv2(), [result])
		x = Lexer(' ')
		self.assertEqual(x.lexv2(), [result])
		x = Lexer('\t')
		self.assertEqual(x.lexv2(), [result])
		x = Lexer('\n')
		self.assertEqual(x.lexv2(), [result])

	def test_comments(self):
		comment_file = 'x'
		non_comment_file = 'y'
		# inline comments before name
		# inline comments after name
		# comment on line before name
		# comment on line after name but before any options
		# comment on line after name after first option
		# comment on line after name before first option
		# comment before tab before first option
		# comment after tab before first option
		# comments after options (should strip off extra spaces )
		# randomly between (newline separated on each end) definitions
		# 	tab indented or not

if __name__ == '__main__':
	unittest.main()