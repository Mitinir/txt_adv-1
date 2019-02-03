from txt_adv_classes import *
from txt_adv_methods import *


print('Welcome to the world')
player_name = input('What is your name?:\n')

player = Player(player_name, 'Start Location',  ['sword', 'cookie', 'README note'])
print('\nHello,', player.name)
print('Your current location is:', player.location)
print('Items in your posession are:', player.items)
answer = input('In front of you is a door, do you open it? yes/no\n')

if(answer=='yes'):
	labos = Labos()
	player_loc = labos
#	player.location = type(player_loc).__name__
	labos.info()
	print('\nItems available in this room are: ', player_loc.items)
else:
	print('fuck you')


itemname = input('To take an item, type TAKE and the name of the item. To skip looting type "no"\n')
instruction, item = input_check(itemname, player_loc)

while instruction!='no':
	
	player.take_item(item, player_loc)

	print('\nYour current items are: ', player.items)
	print('\nCurrent items in the room: ', player_loc.items)
	itemname = input('\n If you would like to take another item, type TAKE and the items name. If not, type "no"')
	instruction, item = input_check(itemname, player_loc)

print('Where do you want to go now?')




