from txt_adv import *

print('Welcome to the world')
player_name = input('What is your name?:\n')

player = Player(player_name, 'Start Location',  ['sword', 'cookie', 'README note'])
print('\nHello,', player.name)
print('Your current location is:', player.location)
print('Items in your posession are:', player.items)
answer = input('In front of you is a door, do you open it? yes/no\n')

if(answer=='yes'):
	labos = Labos()
	print(labos.info())
	player.location = labos.name
	print('\nYour current location is:', player.location)
	print('\nItems available in this room are: ', labos.items)

itemname = input('To take an item, type the name of the item:\n')

while itemname!='no':

	player_loc = labos

	player.take_item(itemname, player_loc) #ne radi jer u txt_adv.py ne pristupa dobro listama kojima treba pristupit

	print('\nYour current items are: ', player.items)
	print('\nCurrent items in the room: ', labos.items)
	itemname = input('\n If you would like to take another item, type its name. If not, type "no"')




