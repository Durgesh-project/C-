#!/usr/bin/env python3
"""Bagels, a deductive logic game.
By me."""
import random

def num_digit():
	return random.randint(3, 5)


def secret_num():
	digit_of_num = num_digit()
	secret = random.randint(10**(digit_of_num-1), 10**digit_of_num)
	return secret, digit_of_num

def each_digit(num, digit_of_num):
	arr = []
	while(num>=1):
		arr.append(num%10)
		num = int(num/10)
	return arr

def starting(digit_of_num):
	print(("I am thinking of a {}-digit number. Try to guess what it is.").format(digit_of_num))
	print("When I say:    That means:")
	print("  Pico         One digit is right but in wrong position.")
	print("  Fermi        One digit is right and in right position.")
	print("  Bagels       No digit is correct.")	
	print("I have thought up of a number.")
	print(" You have 10 guesses to get it.")
	
def clues(secret, guess, digit_of_num):
	sec_num = each_digit(secret, digit_of_num)
	guess_num = each_digit(guess, digit_of_num)
	output = []
	for i in range(len(guess_num)):
		if guess_num[i] == sec_num[i]:
			output.append("Fermi")
		elif guess_num[i] in sec_num:
			output.append("Pico")
	
	output.sort()
	if len(output) == 0:
		print("Bagels", end = " ")
	else :
		j = 0
		while(j < len(output)):
			print(output[j], end = " ")
			j = j+1
	print("")

while("True"):
	secret, digit_of_num = secret_num()
	starting(digit_of_num)
	n = 0
	while(n<10):
		print(("Guess #{}:").format(str(n+1)))
		a_input = input()
		if(len(a_input) != digit_of_num):
			continue
		guess = int(a_input)
		if(guess == secret):
			print("You got it!")
			break
		clues(secret, guess, digit_of_num)
		n = n+1
		
	if(guess != secret):
		print("You ran out of guesses....")
		print(("The answer was {}").format(secret))
		
	print("Do you want to play it ? (yes or no)")
	b_input = input()
	if(b_input) == "no":
		break
	elif(b_input) == "yes":
		continue

print("Thanks for playing!")
	
	
			
		
				
				
	
