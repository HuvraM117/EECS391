# /usr/bin/python3
# Huvra Mehta
# Homework 5 - Problem 2

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.special import comb
from random import randint, shuffle


#generate the five data sets for each of the five hypothesis
def create(bag_num: int) -> list:

	if (bag_num == 1):
		#100% cherry 
		return ["cherry"] * 100


	if (bag_num == 2):
		#75% cherry 25% lime 
		D2 = []
		cherry_list = ["cherry"] * 75
		lime_list = ["lime"] * 25 
		D2.extend(cherry_list)
		D2.extend(lime_list)
		shuffle(D2)
		return D2 

	if (bag_num == 3):
		#50% 50%
		D3 = []
		cherry_list = ["cherry"] * 50
		lime_list = ["lime"] * 50
		D3.extend(cherry_list)
		D3.extend(lime_list)
		shuffle(D3)
		return D3 

	if (bag_num == 4):
		#25% cherry %75 lime 
		D4 = []
		cherry_list = ["cherry"] * 25
		lime_list = ["lime"] * 75 
		D4.extend(cherry_list)
		D4.extend(lime_list)
		shuffle(D4)
		return D4

	if (bag_num == 5):
		#100% lime 
		return ["lime"] * 100

	return 

def likelihood(candy_list: list , hypo_num: int) -> float: 
	#20.3 I get a list of posterior probability at each x 
	prod = 1
	for candy in candy_list: #for each candy in the given candy_list 
		candy_h = posterior_given(candy, hypo_num) #get the probability that it is that candy 
		prod = prod * candy_h #mulitply it all together 
	return prod 

def posterior_given(candy: str, hypo_num: int) -> float:
	
	if(hypo_num == 1): # all cherry
		if(candy == "lime"): 
			return 0
		else:
			return 1

	elif(hypo_num == 2): # 75% cherry

		if(candy == "lime"):
			return 0.25
		else:
			return 0.75

	elif(hypo_num == 3): # 50/50
		return .5

	elif(hypo_num == 4): # 25% cherry
		if(candy == "cherry"): #candy is cherry
			return 0.25
		else:
			return 0.75

	else: #all lime
		if(candy == "cherry"): #candy is cherry
			return 0
		else:
			return 1


#implement given equations to decide which bag it is 
def posterior (candy_list: list, hypo_num: int) -> list:
	h_prob = [0.1, 0.2, 0.4, 0.2, 0.1] 

	data = []

	for i in range(0, len(candy_list)): #get the likelihood at the given length of the the list 
		temp_list = candy_list[0:i]
		like = likelihood(temp_list, hypo_num)
		data.append( like * h_prob[hypo_num - 1])
	return data

def plot(bag_num: int):

	candy_list = create(bag_num)
	h1 = posterior(candy_list, 1) 
	h2 = posterior(candy_list, 2)
	h3 = posterior(candy_list, 3)
	h4 = posterior(candy_list, 4)
	h5 = posterior(candy_list, 5)

	for i in range(0 , len(candy_list)): #normalize! 
		d1 = h1[i]
		d2 = h2[i]
		d3 = h3[i]
		d4 = h4[i]
		d5 = h5[i]

		sum = d1 + d2 + d3 + d4 + d5 

		h1[i] = d1/sum 
		h2[i] = d2/sum 
		h3[i] = d3/sum 
		h4[i] = d4/sum 
		h5[i] = d5/sum 

	plt.figure(1)
	plt.subplot(1,2,1)

	x = range(0, len(candy_list))
	plt.plot(x, h1, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=5)
	plt.plot(x, h2, color='orange', marker='o', linestyle='solid', linewidth=2, markersize=5)
	plt.plot(x, h3, color='blue', marker='o', linestyle='dashdot', linewidth=2, markersize=5)
	plt.plot(x, h4, color='purple', marker='o', linestyle='dotted', linewidth=2, markersize=5)
	plt.plot(x, h5, color='magenta', marker='o', linestyle='dashed', linewidth=2, markersize=5)
	plt.gca().legend(('h1','h2', 'h3', 'h4', 'h5'))


	pred_val = []

	next_h1 = posterior_given("lime", 1)
	next_h2 = posterior_given("lime", 2)
	next_h3 = posterior_given("lime", 3)
	next_h4 = posterior_given("lime", 4)
	next_h5 = posterior_given("lime", 5)

	for i in range(0, len(h1)):
		val1 = next_h1 * h1[i]
		val2 = next_h2 * h2[i]
		val3 = next_h3 * h3[i]
		val4 = next_h4 * h4[i]
		val5 = next_h5 * h5[i]
		pred_val.append(val1 + val2 + val3 + val4 + val5)

	plt.subplot(1,2,2)
	plt.plot(x, pred_val, color='magenta', marker='*', linestyle='dashed', linewidth=2, markersize=5)
	plt.show()

#plot(1)
#plot(2)
#plot(3)
#plot(4)
#lot(5)

def plot2 (): 

	candy_list1 = create(1)
	candy_list2 = create(2)
	candy_list3 = create(3)
	candy_list4 = create(4)
	candy_list5 = create(5)

	hypo = 1
	while (hypo != 6):
		d1 = posterior(candy_list1, hypo)
		d2 = posterior(candy_list2, hypo)
		d3 = posterior(candy_list3, hypo)
		d4 = posterior(candy_list4, hypo)
		d5 = posterior(candy_list5, hypo)

		f_list = []

		for i in range(0, len(d1)): #average it all together 
			sum = d1[i] + d2[i] + d3[i] + d4[i] + d5[i]
			f_list.append( sum/5 )

		x = range(0, len(candy_list1), 1)
		plt.plot(x, f_list)
		hypo = hypo + 1

	plt.gca().legend(('h1','h2', 'h3', 'h4', 'h5'))
	plt.show()

plot2()








