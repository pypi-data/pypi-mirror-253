class GeneratorSyntaxError(Exception):
	pass

def gerund(verb):
	if verb[-1] == 'e':
		return(f'{verb[:-1]}ing')
	elif verb[-2:] == 'ot':
		return(f'{verb}ting')
	elif verb[-2:] == 'el':
		return(f'{verb}ling')
	else:
		return(f'{verb}ing')

def past_participle(verb):
	if verb.lower() == 'wake':
		return('Woken')
	elif verb.lower() == 'rise':
		return('Risen')
	elif verb[-1] == 'e':
		return(f'{verb}d')
	elif verb[-2:] == 'ot':
		return(f'{verb}ted')
	else:
		return(f'{verb}ed')

def pluralize(word):
	return(''.join(_pluralize(word)))

def _pluralize(word):
	if word.lower() == 'goose':
		return('geese', '')
	if any(word.lower().endswith(test) for test in ['knife', 'life', 'wife']):
		return(word[-2], 'ves')
	if word.lower() in {'beef', 'carp', 'cod', 'deer', 'perch', 'potatoes', 'sheep', 'squid', 'woods' }:
		return(word, '')
	if word[-1] in {'s', 'x', 'z'}:
		return(word, 'es')
	if word[-2:] in {'ch', 'sh'}:
		return(word, 'es')
	if word[-1] == 'f':
		return(word[:-1], 'ves')
	if word[-2:] == 'ey':
		return(word[:-2], 'ies')
	if word[-1] == 'y':
		return(word[:-1], 'ies')
	return(word, 's')

def lowercase(word):
	return(word.lower())

def TitleCase(word):
	return(word.title())

def alliterate(list1, separator, list2):
	pass

def unique(list1, separator, list2):
	pass
