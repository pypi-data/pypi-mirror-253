import argparse

from lexer import Lexer
from parser import Parser
from interpreter import TreeWalkInterpreter

import makeshift.interpreter.ast
import makeshift.file_printer
import makeshift.ast_printer

def test_lexer(filename = None):
	if filename is None:
		filename = input('Enter a .txt file to parse: ')
		if filename.strip() == '':
			filename = 'inn.txt'
			print('No file name entered. Using inn.txt')
	print(f'Lexing {filename}\n')

	result = run_lexer_v2(filename)
	for token in result.tokens:
		print(token)

def compare_lexers(filename = None):
	if filename is None:
		filename = input('Enter a .txt file to parse: ')
		if filename.strip() == '':
			filename = 'inn.txt'
			print('No file name entered. Using inn.txt')
	
	v1 = run_lexer(filename)
	v2 = run_lexer_v2(filename)
	print(v1.tokens == v2.tokens)

	for idx, token in enumerate(v1.tokens):
		if token != v2.tokens[idx]:
			print(f'{token} != {v2.tokens[idx]}')


def run_lexer(filename):
	"""Return a list containing the tokens
	from the given filename
	"""
	with open(filename) as inp_file:
		x = Lexer(inp_file.read())
		x.lex()
	return(x)

def run_lexer_v2(filename):
	with open(filename) as inp_file:
		x = Lexer(inp_file.read())
		x.lexv2()
	return(x)

def test_ast_print():
	gen = create_simple_ast()
	printer = ast_printer.AstPrinter()
	printer.print_ast(node = gen)

def create_simple_ast():
	"""
	manually builds a simple AST for the below generator
	returns the generator node

	Inn
		{Name}

	Name
		Inn of the {descriptor} {thing} 10%
		The {descriptor} {noun} 10%
		The {creature}'s {place | item.plural}
		The {item} {place}
		{noun} and {noun}
	"""

	#defining all the literals and terminals
	inn = ast.Name("Inn")
	name = ast.Name("Name")
	descriptor = ast.Name("descriptor")
	thing = ast.Name("thing")
	creature = ast.Name("creature")
	place = ast.Name("place")
	item = ast.Name("item")
	noun = ast.Name("noun")

	str1 = ast.String_Literal("Inn of the ")
	str2 = ast.String_Literal("The ")
	str3 = ast.String_Literal("'s ")
	str4 = ast.String_Literal(" ")
	str5 = ast.String_Literal(" and ")

	plural = ast.Method(method_name = "plural")

	#all the parts where we point to (reference) another name in brackets
	inn_ref = ast.Reference(name = inn)
	name_ref = ast.Reference(name = name)
	descriptor_ref = ast.Reference(name = descriptor)
	thing_ref = ast.Reference(name = thing)
	creature_ref = ast.Reference(name = creature)
	place_ref = ast.Reference(name = place)
	item_ref = ast.Reference(name = item)
	item_plural_ref = ast.Reference(name = item, method = plural)
	noun_ref = ast.Reference(name = noun)

	#Resolvables, groups of references or other expressions
	name_resolvable = ast.Resolvable([name_ref])
	descriptor_resolvable = ast.Resolvable([descriptor_ref])
	thing_resolvable = ast.Resolvable([thing_ref])
	creature_resolvable = ast.Resolvable([creature_ref])
	place_resolvable = ast.Resolvable([place_ref])
	item_resolvable = ast.Resolvable([item_ref])
	place_item_plural_resolvable = ast.Resolvable([place_ref, item_plural_ref])
	noun_resolvable = ast.Resolvable([noun_ref])

	#Individual expressions
	#{Name}
	expression1 = ast.Expression([name_resolvable])

	#Inn of the {descriptor} {thing} 10%
	expression2 = ast.Expression([
		str1, descriptor_resolvable, str4, thing_resolvable])

	#The {descriptor} {noun} 10%
	expression3 = ast.Expression([
		str2, descriptor_resolvable, str4, noun_resolvable])

	#The {creature}'s {place | item.plural}
	expression4 = ast.Expression([
		str2, creature_resolvable, str3, place_item_plural_resolvable])

	#The {item} {place}
	expression5 = ast.Expression([
		str2, item_resolvable, str4, place_resolvable])

	#{noun} and {noun}
	expression6 = ast.Expression([
		noun_resolvable, str5, noun_resolvable])

	option1 = ast.Option(expression1)
	option2 = ast.Option(expression2, 10)
	option3 = ast.Option(expression3, 10)
	option4 = ast.Option(expression4)
	option5 = ast.Option(expression5)
	option6 = ast.Option(expression6)

	definition1 = ast.Definition(name = inn, options = [option1])
	definition2 = ast.Definition(name = name, options = [option2,
		option3, option4, option5, option6])

	generator = ast.Generator(title = 'inn.txt', 
		top_definition = definition1,
		definitions = [definition1, definition2])

	return(generator)

def test_FilePrinter_visitor():
	#run the FilePrinter() visitor on the simple ast created
	#by create_simple_ast()
	gen = create_simple_ast()
	file_printer.FilePrinter().display(gen)

def run_from_cli():
	cli_parser = argparse.ArgumentParser(
		description = "Run a Random Generator")

	cli_parser.add_argument('infile',
		help = 'Generator file to run',
		type = argparse.FileType('r'))
	cli_parser.add_argument('-c', '--count',
		help = 'Number of examples to generate',
		type = int, default = 1)

	args = cli_parser.parse_args()
	if args.infile == '' or args.infile is None:
		cli_parser.print_help()
		return

	x = Lexer(args.infile.read())
	x.lexv2()
	args.infile.close()

	pr = Parser(x.tokens)
	ast = pr.generator(args.infile.name)
	
	# printer = ast_printer.AstPrinter()
	# printer.print_ast(node = ast)

	interp = TreeWalkInterpreter()
	if args.count == 1:
		print(f'{interp.visit_generator_node(ast)}')
		return
	
	for x in range(0,args.count):
		print(f'{x+1:>2}. {interp.visit_generator_node(ast)}')


if __name__ == '__main__':
	run_from_cli()
