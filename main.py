# imports
import random as rd
import colorama
from colorama import Style, Fore, init

colorama.init() # colorama initialization

print('Hello!')

male_names = ('Liam', 'Noah', 'William', 'James', 'Oliver', 
	'Benjamin', 'Lucas', 'Mason', 'Jack', 'Alexander', 
	'Ethan', 'Michael', 'Jacob', 'Daniel', 'Henry', 
	'David', 'Joseph', 'John', 'Carter', 'Owen', 
	'Luke', 'Dylan', 'Andrew', 'Leo', 'Robert')

female_names = ('Emma', 'Olivia', 'Ava', 'Sophia', 'Mia', 
	'Evelyn', 'Emily', 'Harper', 'Ella', 'Elizabeth', 
	'Luna', 'Victoria', 'Camila', 'riley', 'Lily', 
	'Hannah', 'Lillian', 'Aubrey', 'Gillian', 'Zoey', 
	'Hazel', 'Bella', 'Lucy', 'Ann', 'Alice')

lastnames = ('Anderson', 'Smith', 'Williams', 'Jones', 'Taylor', 
	'Moore', 'Harris', 'White', 'Morgan', 'Bell', 
	'Cooper', 'Lee', 'Walker', 'Allen', 'Hill', 
	'King', 'Green', 'Carter', 'Perry', 'Mitchel', 
	'Evans', 'Foster', 'Flores', 'Henderson', 'Wright')

# function
def generate():
	print(Fore.WHITE)
	sex = input('Male or female? Enter "m" or "f" -> ') # asking about name
	# male name
	if sex.lower() == 'm':
		print(Fore.GREEN)
		first_name = rd.choice(male_names)
		last_name = rd.choice(lastnames)
		print('{} {}'.format(first_name, last_name))

	# female name	
	elif sex.lower() == 'f':
		print(Fore.GREEN)
		first_name = rd.choice(female_names)
		last_name = rd.choice(lastnames)
		print('{} {}'.format(first_name, last_name))

	# another situations	
	else:
		print(Fore.RED)
		print('What? Repeat, please!')

generate()

# repeating
while True:
	print(Fore.WHITE)
	try_again = input('Again? Enter "y" or "Enter" for exit  -> ') # asking for one more time
	# try again
	if try_again.lower() == 'y':
		generate()
	# do not try again	
	else:
		break