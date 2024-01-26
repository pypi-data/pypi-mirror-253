
import argparse
import sys
from pathlib import Path

from makeshift.interpreter.lexer import Lexer
from makeshift.interpreter.parser import Parser
from makeshift.interpreter.interpreter import TreeWalkInterpreter

def parse_cli_args():
	parser = argparse.ArgumentParser(
		description = "Run a Random Generator")

	parser.add_argument('input_file',
		help = 'MakeShift template file to run')
	parser.add_argument('-c', '--count',
		help = 'Number of examples to generate',
		type = int, default = 1)

	args = parser.parse_args()

	if args.input_file == '' or args.input_file is None:
		parser.print_help()
		return(None)

	return(args)

def main():

	args = parse_cli_args()
	if args is None:
		sys.exit(2)

	filename = find_file(args.input_file)
	with open(filename) as gen_file:
		x = Lexer(gen_file.read())

	x.lexv2()

	pr = Parser(x.tokens)
	ast = pr.generator(args.input_file)

	interp = TreeWalkInterpreter()
	if args.count == 1:
		print(f'{interp.visit_generator_node(ast)}')
		return
	
	for x in range(0,args.count):
		print(f'{x+1:>2}. {interp.visit_generator_node(ast)}')

def find_file(filename):
	if Path(filename).exists():
		return(filename)
	elif Path('examples', filename).exists():
		return(Path('examples', filename))