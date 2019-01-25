from txt_adv import *

print('Welcome to the world')
player_name = input('What is your name?:\n')

player = Player(player_name, 'Start Location',  ['sword', 'cookie', 'README note'])
print('\nyour name is:', player.name)
print('your current location is:', player.location)
print('items in your posession are:', player.items)
answer = input('In front of you is a door, do you open it?')

if(answer=='yes'):
	labos = Labos()
	print(labos.info) #ne printa labos.info jer nije dobro definiran pristup metodi nadklase
	player.location = labos.name
	print('your current location is:', player.location)
	print('items available in this room are: ', labos.items)

else:
	print('are you sure?')

itemname = input('to take an item, type the name of the item')

player.take_item(itemname, player.location) #ne radi jer u txt_adv.py ne pristupa dobro listama kojima treba pristupit

print('your current items are: ', player.items)
print('current items in the room: ', labos.items)



