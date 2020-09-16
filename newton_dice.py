import sys
import random

def dice_roll(dice_num):
	num_of_six = dice_num/6
	count_of_six = 0
	for i in range(dice_num):
		dice_roll = random.randint(1, 6)
		if(dice_roll == 6):
			count_of_six += 1

	if(count_of_six >= num_of_six):
		return True
	else:
		return False


def dice_probability(iterations):
	rolls = [0, 0, 0]
	for i in range(iterations):
		if dice_roll(6):
			rolls[0] += 1
		if dice_roll(12):
			rolls[1] += 1
		if dice_roll(18):
			rolls[2] += 1


	return rolls
	

def main():

	iterations = 100000
	rolls_probability_6_to_18 = dice_probability(iterations)

	for i in range(len(rolls_probability_6_to_18)):
		print('Probability of rolling {:.0f} six(es) in {:.0f} dices: {:.4f}%'
		.format(i+1, (i+1)*6, rolls_probability_6_to_18[i]/iterations*100))


main()