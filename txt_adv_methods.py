Instructions = ['TAKE', 'ENTER']  #a list containing KEYWORDS used in the game for commands
#remainder: set the list to be a dictionary do that the KEYWORD invokes a method by itself

#splits user input to extract the KEYWORD which should be located in the list Instructions
def split_input_KEYWORD(user_input):
	instruction = user_input.split()[0]
	while instruction not in Instructions:
		instruction = input('I do not know of this KEYWORD! Try again please: \n')
	return instruction

#splits the user input to extract the ITEM name or command specifics in the future 
def split_input_ITEM(user_input, current_location):
	instruction = user_input.split()[0]  #splits the input at indice 0 - extracts the first word
	partial = user_input.split(instruction + ' ') #strips the space between the first and second word
	try:
		item = partial[1] #if there exists any other word except the first one in user input
		if item not in current_location.items:  #if ITEM specified exists in the current room
			print('Sorry, that item is not in this room!\n')
		else:
			return item
	except IndexError:
		print('You did not specify an item to loot!\n')

#cheks user input if the partials are KEYWORDS or ITEMS that exist 
def input_check(user_input, current_location):
	if user_input=='no':
		return 'no', 'no'
	instruction = split_input_KEYWORD(user_input) 
	item = split_input_ITEM(user_input, current_location)

	while instruction not in Instructions or item not in current_location.items:
		inst = input('Please enter a valid command!\n')
		instruction = split_input_KEYWORD(inst) 
		item = split_input_ITEM(inst, current_location)
	return instruction, item

