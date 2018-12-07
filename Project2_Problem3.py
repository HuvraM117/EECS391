#Huvra Mehta (HSM20)

#Import Necessary Libraries 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math as math
import random
import csv

petal_length = []
petal_width  = []
species_data = []

def data() -> None:
	with open('irisdata.csv', mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			petal_width.append(float(row['petal_width']))
			petal_length.append(float(row['petal_length']))
			species_data.append(row['species'])

def neuralNetwork_NoThreshold(x: float, y: float, w1: float, w2: float, bias: float) -> float: 
	z = ((w1*x) + (w2*y) + bias)
	sigmoid = 1 / (1 + math.exp(-z))
	return sigmoid

def MSE(dataset:list, w1: float, w2: float, bias: float) -> None: 
	
	sum = 0

	for d in range (0, len(dataset)):
		x = dataset[d,1]
		y = dataset[d,2]

		value = neuralNetwork_NoThreshold(x, y, w1, w2, bias)

		sum = sum + (value - dataset[d,0])**2 #predicition - actual value squared 

	final = sum / len(dataset)

	return final 

def gradient(dataset:list, w1: float, w2: float, bias: float, x_list: list) -> float: 

	sum = 0 
	val = 1
	val2 = 1 
	val3 = 1

	for d in range (0, len(dataset)):
		x = dataset[d,1]
		y = dataset[d,2]

		value = neuralNetwork_NoThreshold(x, y, w1, w2, bias)
		val = (value - dataset[d,0]) #predicition - actual value squared 
		val2 = value 
		val3 = (1 - value)
		sum = sum + (val * val2 * val3 * x_list[d])

	final = sum * 2 / len(dataset)

	return final 

def learningCurge(MSE_list: list, count: int) -> None: 
	x = range(count)
	plt.plot(x, MSE_list, 'g-', linewidth=2, markersize=12)
	plt.show()


def plot(dataset:list , w1: float, w2: float, bias: float) -> None: 

	x = []
	y = []

	for d in range (0, len(dataset)):
		x_value = (dataset[d, 1])
		x.append(x_value)
		y.append((((-1 * w1) * x_value) - bias)/w2)

	plt.figure(1)
	colmap = {0: 'x', 1: 'v'}
	for d in range(0,len(dataset)):
		plt.scatter(dataset[d, 1], dataset[d,2], s=7, marker = colmap[dataset[d,0]])

	plt.plot(x, y, 'g-', linewidth=2, markersize=12)

	plt.title("Excercise 3")
	plt.xlabel('Petal Length')
	plt.ylabel('Petal Width')

	plt.show()


def callGradient(dataset:list) -> None: 

	w1 = random.random()
	w2 = random.random()
	bias = random.uniform(-10, -1)

	w1_copy = 0
	w2_copy = 0
	bias_copy = 0

	x = []
	y = []
	z = [1] * len(dataset)

	for d in range (0, len(dataset)):
		x.append(dataset[d,1])
		y.append(dataset[d,2])

	mse_list = [] 

	mse = MSE(dataset, w1, w2, bias)
	mse_list.append(mse)
	mse_copy = 0 

	count = 1

	plot(dataset, w1, w2, bias)
	learningCurge(mse_list, count)

	while(abs(w1 - w1_copy) > .0002) or (abs (w2 - w2_copy)  > .0002) or (abs (bias - bias_copy)  > .0002):

		w1_copy = w1
		w2_copy = w2
		bias_copy = bias

		w1 = w1 - (gradient(dataset, w1, w2, bias, x) * .05)
		w2 = w2  - (gradient(dataset, w1, w2, bias, y)  * .05)
		bias = bias  - (gradient(dataset, w1, w2, bias, z)  * .05)

		mse = MSE(dataset, w1, w2, bias)
		mse_list.append(mse)

		count = count + 1

		if(count == 700):
			plot(dataset, w1, w2, bias)
			learningCurge(mse_list, count)

	plot(dataset, w1, w2, bias)
	learningCurge(mse_list, count)


def main() -> None: 

	#create dataset
	data()

	species = []
	length = []
	width = []

	for p in range (50, len(petal_length)):
		if (species_data[p] == 'versicolor'):
			species.append(0)
		if (species_data[p] == 'virginica'):
			species.append(1)
		length.append(petal_length[p])
		width.append(petal_width[p])


	df = pd.DataFrame({
			'x': length,
			'y': width,
			's': species
		})

	# Change dataframe to numpy matrix
	dataset = df.values[:, 0:4]

	callGradient(dataset)

main()









