"""
The interpreter takes the Abstract Syntax Tree from the parser and 
recursively executes it starting from the highest, most general node
"""

import random

from makeshift.interpreter import utils
from makeshift.interpreter import ast

class TreeWalkInterpreter(ast.Visitor):

	def __init__(self):
		self.chooser = self.weight_based_choice
		self.string_method = self.basic_string

	def choose(self, choices, weights):
		return(self.chooser(choices, weights))

	@staticmethod
	def basic_string(string):
		return(string)

	@staticmethod
	def weight_based_choice(choices, weights):
		return(random.choices(population = choices, weights = weights)[0])

	def visit_generator_node(self, generator):
		self.defs = {definition.name.value: definition for definition in generator.definitions}
		return(generator.top_definition.accept_visitor(self))

	def visit_definition_node(self, definition):
		#get the percentage for each option
		#pick an option based on weights
		#run the option
		temp = []
		weights = []
		for option in definition.options:
			if option.percent:
				temp.append(int(option.percent))
			else:
				temp.append(0)

		s = (100 - sum(temp)) / max(temp.count(0), 1)
		for weight in temp:
			if weight == 0:
				weights.append(s)
			else:
				weights.append(weight)

		#option = random.choices(population = definition.options, weights = weights)[0]
		option = self.choose(definition.options, weights)
		return(option.accept_visitor(self))

	def visit_name_node(self):
		raise NotImplementedError

	def visit_option_node(self, option):
		return(option.expression.accept_visitor(self))

	def visit_expression_node(self, expression):
		string = ''
		for subexpression in expression.subexpressions:
			string += subexpression.accept_visitor(self)
		return(string)

	def visit_resolvable_node(self, resolvable):
		selection = random.choice(resolvable.segments)
		return(selection.accept_visitor(self))

	def visit_reference_node(self, ref):
		definition = self.defs[ref.name.value]
		prev_choice = None
		prev_str = None
		
		if ref.method:
			prev_choice = self.chooser
			prev_str = self.string_method
			ref.method.accept_visitor(self)
		
		result = definition.accept_visitor(self)
		
		if prev_choice is not None:
			self.chooser = prev_choice
		if prev_str is not None:
			self.string_method = prev_str
		return(result)

	def visit_string_literal_node(self, str_lit):
		if self.string_method:
			return(self.string_method(str_lit.value))
		else:
			return(f'{str_lit.value}')

	def visit_method_node(self, method):
		if method.method_name == 'plural':
			self.string_method = utils.pluralize
		elif method.method_name == 'gerund':
			self.string_method = utils.gerund
		elif method.method_name == 'lowercase':
			self.string_method = utils.lowercase
		elif method.method_name == 'TitleCase':
			self.string_method = utils.TitleCase
		elif method.method_name == 'past_participle':
			self.string_method = utils.past_participle
		else:
			raise NotImplementedError