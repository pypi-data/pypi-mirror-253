import makeshift.interpreter.ast as ast

class FilePrinter(ast.Visitor):
	"""
	create the human-readable version of a given AST node
	"""

	def display(self, node):
		print(node.accept_visitor(self))

	def visit_generator_node(self, generator):
		string = generator.title + '\n'
		for definition in generator.definitions:
			string += definition.accept_visitor(self)
			string += '\n'
		return(string)

	def visit_definition_node(self, definition):
		string = definition.name.accept_visitor(self)
		string += '\n'
		for option in definition.options:
			string += '\t'
			string += option.accept_visitor(self)
			string += '\n'
		return(string)

	def visit_name_node(self, name):
		 return(f'{name.value}')

	def visit_option_node(self, option):
		string = option.expression.accept_visitor(self)
		if option.percent is not None:
			string += f' {option.percent}%'
		return(string)

	def visit_expression_node(self, expression):
		string = ''
		for subex in expression.subexpressions:
			string += subex.accept_visitor(self)
		return(string)

	def visit_resolvable_node(self, resolvable):
		string = '{'
		s = '|'.join([segment.accept_visitor(self) for segment in resolvable.segments])
		# for segment in resolvable.segments:
		# 	string += segment.accept_visitor(self)
		string += s
		string += '}'
		return(string)

	def visit_reference_node(self, ref):
		string = ref.name.accept_visitor(self)
		if ref.method:
			string += f'.{ref.method.accept_visitor(self)}'
		return(string)

	def visit_string_literal_node(self, str_lit):
		 return(f'{str_lit.value}')

	def visit_method_node(self, method):
		 return(f'{method.method_name}')