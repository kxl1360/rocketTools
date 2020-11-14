import sys
import random
def do_work():
	""" Function to handle command line usage"""
	args = sys.argv
	args = args[1:] # First element of args is the file name
	if len(args) == 0:
		print('You have not passed any commands in!')
	else:
		for a in args:
			if a == '--help':
				print('Basic command line program')
				print('Options:')
				print('    --help -> show this basic help menu.')
				print('    --monty -> show a Monty Python quote.')
				print('    --veg -> show a random vegetable')
			elif a == '--monty':
				print('What\'s this, then? "Romanes eunt domus"? People called Romanes, they go, the house?')
			elif a == '--veg':
				print(random.choice(['Carrot', 'Potato', 'Turnip']))
			else:
				print('Unrecognised argument.')
if __name__ == '__main__':
	do_work()