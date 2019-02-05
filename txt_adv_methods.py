from txt_adv_classes import *

#Instructions is a dictionary mapping KEYORDS to object methods
Instructions = { 'TAKE': Player.take_item }


#splits user input to extract the KEYWORD which should be located in the list Instructions
def split_input_KEYWORD(user_input):
	instruction = user_input.split()[0]
	if instruction not in Instructions:
		print('Sorry! I do not know of this KEYWORD')
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
def input_check(player_obj, user_input, current_location):
	if user_input=='no':
		return 'no'
	instruction = split_input_KEYWORD(user_input) 
	item = split_input_ITEM(user_input, current_location)

	while instruction not in Instructions or item not in current_location.items:
		inst = input('Please enter a valid command! Or enter "Q" to quit\n')
		if inst == 'Q':
			break
		instruction = split_input_KEYWORD(inst) 
		item = split_input_ITEM(inst, current_location)

	Instructions[instruction](player_obj, item, current_location)

	return instruction

