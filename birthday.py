#!/usr/bin/env python3
import random
import datetime

def birth_date(Num_of_people,condition):
	month_var = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	start_date = datetime.date(2024,1,1)
	b_date_array = []
	if(condition == True):
		print("Here are {} birthdays:".format(Num_of_people))
	for x in range(0,Num_of_people):
		Random_date = start_date + datetime.timedelta(random.randint(0,365))
		for n,month in enumerate(month_var):
			if(Random_date.month == n+1):
				b_date = month + " " + str(Random_date.day)
				b_date_array.append(b_date)
				if(condition == True):
					print(b_date, end = ", ")
				
	maximum = 1
	for i in range(0, len(b_date_array)):
		y = b_date_array.count(b_date_array[i])
		if maximum < y:
			maximum = y
	
	if(condition == True):
		print("")
		print('In this simulation, ', end='')
		if maximum > 1:
    			print('multiple people have a birthday on {}'.format(b_date))
		else:
			print('there are no matching birthdays.')
		print("")
	return maximum
	
def Simulations(Num_of_people):
	Simulation1 = birth_date(Num_of_people,True)
	print('Generating', Num_of_people, 'random birthdays 100,000 times...')
	input('Press Enter to begin...')
	print("Let's run another 100,000 simulations.")
	count = 0
	for simulations in range(0,100000):
		Same_day = birth_date(Num_of_people,False)
		if Same_day > 1:
			count = count + 1
		if simulations%10000 == 0:
			print(simulations, "simulations run....")
	print('100,000 simulations run.')
	probability = round(count / 100000 * 100, 2)
	print('Out of 100,000 simulations of', Num_of_people, 'people, there was a')
	print('matching birthday in that group', count, 'times. This means')
	print('that', Num_of_people, 'people have a', probability, '% chance of')
	print('having a matching birthday in their group.')
	print("That's probably more than you would think!")
		
	

print('''Birthday Paradox,

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

while True:
	print('How many birthdays shall I generate? (Max 100)')
	response = input('> ')
	if 1 <= int(response) <= 100 :
		Num_of_people = int(response)
		break

Simulations(Num_of_people)



		
