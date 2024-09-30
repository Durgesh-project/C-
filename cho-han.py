#!/usr/bin/env python3
import random

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
			4: 'SHI', 5: 'GO', 6: 'ROKU'}
def dice_throw():
	dice1 = random.randint(1,6)
	dice2 = random.randint(1,6)
	return dice1, dice2
	
def result(dice1 , dice2, bet):
	sum_ = dice1 + dice2
	if((sum_%2 == 0 and bet == 'cho') or (sum_%2 != 0 and bet == 'han')):
		win = True
	else:
		win = False
	return win
		
print("Cho-han")
print("In this traditional Japanese dice game, two dice are rolled in a bamboo")
print("cup by the dealer sitting on the floor. The player must guess if the")
print("dice total to an even (cho) or odd (han) number.")

curr_money = 5000
while(True):
	print()
	print("You have {} mon. How much do you bet? (or QUIT)".format(curr_money))
	response = input("> ")
	print()
	if(response.upper() == "QUIT"):
		print("Thanks for playing!")
		break
	bet_money = int(response)
	if(bet_money > curr_money):
		print("You don't have {} mon in hand".format(bet_money))
		continue
	print("The dealer swirls the cup and you hear the rattle of dice.")
	print("The dealer slams the cup on the floor, still covering the")
	print("dice and asks for your bet.")
	dice1, dice2 = dice_throw()
	print()
	while(True):
		print("    CHO (even) or HAN (odd)?")
		bet = (input("> ")).lower()
		if(bet == 'cho' or bet == 'han'):
			break
	print("The dealer lifts the cup to reveal:")
	print("   {} - {}".format(JAPANESE_NUMBERS[dice1],JAPANESE_NUMBERS[dice2]))
	print("    {} - {}".format(dice1, dice2))
	result_of_throw = result(dice1, dice2, bet)
	if(result_of_throw):
		print("You won! You take {} mon.".format(bet_money*2))
		print("The house collects a {} mon fee.".format(bet_money//10))
		curr_money += (bet_money - bet_money//10)
	else:
		print("You lost!")
		curr_money -= bet_money
	if(curr_money == 0):
		print("You ran out of money......")
		print("Thanks for playing!")
		break

