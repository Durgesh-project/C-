#!/usr/bin/env python3
def decrypt(code):
	to_be_transformed = code.split()
	secret = ""
	for key in range(0,26+1):
		for word in to_be_transformed:
			for letter in word:
				secret += chr(ord(letter) - int(key))
			secret += " "
		print("#For key{}: ".format(key) + secret)
		secret = ''

while(True):
	print("Enter the encrypted Caesar cipher message to hack.")
	code = input("> ")
	decrypt(code)
	print("Do you want to hack another code?")
	response = input("> ")
	response.lower()
	if(response == 'yes'):
		continue
	else:
		break
