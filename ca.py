#!/usr/bin/env python3
#import pyperclip as pc
def encrypt(secret, key):
	to_be_transformed = secret.upper().split()
	code = ""
	for word in to_be_transformed:
		for letter in word:
			code += chr(ord(letter) + int(key))
		code += " "
	return code
		
def decrypt(code, key):
	to_be_transformed = code.split()
	secret = ""
	for word in to_be_transformed:
		for letter in word:
			secret += chr(ord(letter) - int(key))
		secret += " "
	return secret
	
def task_to_do(task):
	maxValue = 0
	message = ''
	if(task.startswith('e')):
		maxValue = 25
		task = 'encrypt'
	else:
		maxValue = 26
		task = 'decrypt'
	print("Please enter the key (0 to {}) to use.".format(maxValue))
	key = input("> ")
	print("Enter the message to {}.".format(task))
	info = input("> ")
	if(task.startswith('e')):
		message = encrypt(info,key)
	else:
		message = decrypt(info,key)
	'''pc.copy(message)
	text = pc.paste()
	print(text)'''
	print(message)
	#print("Full {}ed text copied to clipboard.".format(task))

print("Caesar Cipher")
while(True):
	print("Do you want to (e)ncrypt or (d)ecrypt?")
	task = input("> ").lower()
	if(task.startswith('e') or task.startswith('d')):
		task_to_do(task)
		break
	else:
		print("Please enter 'e' or 'd'")


