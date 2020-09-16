import sys
import random

def monty_hall_probability(iterations, switch):
	prize_count = 0
	for i in range(iterations):
		doors = [0, 0, 0]
		doors[random.randint(0, 2)] = 1
		
		pick = random.randint(0, 2)
		if(switch):
			doors.pop(pick)
			doors.pop(doors.index(0))
			pick = 0
			if(doors[pick]):
				prize_count += 1

		else:
			if(doors[pick]):
				prize_count += 1


	return prize_count/iterations*100


def main():
	print('Monty hall problem!')
	iterations = 1000000
	switch = int(input('Enter "1" to switch and "0" to keep the same door: '))
	probability = monty_hall_probability(iterations, switch)
	if(switch):
		print('Probabilty if you switch the door: {}%, in {} iteratons.'.format(probability, iterations))
	else:
		print('Probabilty if you keep the door: {}%, in {} iterations.'.format(probability,iterations))


main()