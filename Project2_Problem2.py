#Huvra Mehta (HSM20)

#Import Necessary Libraries 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math as math
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


def neuralNetwork(x: float, y: float, w1: float, w2: float, bias: float) -> float: 
	z = ((w1*x) + (w2*y) + bias)
	sigmoid = 1 / (1 + math.exp(-z))

	if (sigmoid < .5):
		return 0
	else:
		return 1


def problem2a(dataset:list, w1: float, w2: float, bias: float) -> None: 
	
	sum = 0

	for d in range (0, len(dataset)):
		x = dataset[d,1]
		y = dataset[d,2]

		value = neuralNetwork(x, y, w1, w2, bias)

		sum = sum + (value - dataset[d,0])**2 #predicition - actual value squared 

	final = sum / len(dataset)

	return final 


def problem2b(dataset: list) -> None: 
	Aw1 = .4
	Aw2 = .7
	Abias = -3.2

	Bw1 = .3
	Bw2 = .7
	Bbias = -3.2

	print("Mean Squared Error for First Set of Weights: ")
	print("W1", Aw1)
	print("W2", Aw2)
	print("BIAS", Abias)
	print("Mean Squared Error: ", problem2a(dataset, Aw1, Aw2, Abias))

	print("Mean Squared Error for Second Set of Weights: ")
	print("W1", Bw1)
	print("W2", Bw2)
	print("BIAS", Bbias)
	print("Mean Squared Error: ", problem2a(dataset, Bw1, Bw2, Bbias))

	plot2b(dataset)


def plot2b(dataset) -> None: 
	colmap = {0: 'x', 1: 'v'}
	for d in range(0,len(dataset)):
		plt.scatter(dataset[d, 1], dataset[d,2], s=7, marker = colmap[dataset[d,0]])

	Aw1 = .4
	Aw2 = .7
	Abias = -3.2

	Bw1 = .3
	Bw2 = .7
	Bbias = -3.2

	x = []
	y1 = []
	y2 = []  

	for d in range (0, len(dataset)):
		x_value = (dataset[d, 1])
		x.append(x_value)
		y1.append((((-1 * Aw1) * x_value) - Abias)/Aw2)
		y2.append((((-1 * Bw1) * x_value) - Bbias)/Bw2)

	plt.plot(x, y1, 'g-', linewidth=2, markersize=12)
	plt.plot(x, y2, 'r-', linewidth=2, markersize=12)

	plt.title("Excercise 2. B")
	plt.xlabel('Petal Length')
	plt.ylabel('Petal Width')

	plt.show()


def neuralNetwork_NoThreshold(x: float, y: float, w1: float, w2: float, bias: float) -> float: 
	z = ((w1*x) + (w2*y) + bias)
	sigmoid = 1 / (1 + math.exp(-z))
	return sigmoid


def problem2e(dataset:list, w1: float, w2: float, bias: float, x_list: list) -> float: 

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


def callProblem2e(dataset:list) -> None: 

	Aw1 = .4
	Aw2 = .7
	Abias = -3.2

	Bw1 = .3
	Bw2 = .7
	Bbias = -3.2

	x = []
	y = []
	z = [1] * len(dataset)

	for d in range (0, len(dataset)):
		x.append(dataset[d,1])
		y.append(dataset[d,2])

	Aw1_new = Aw1 - (problem2e(dataset, Aw1, Aw2, Abias, x) * .1)
	Aw2_new = Aw2  - (problem2e(dataset, Aw1, Aw2, Abias, y)  * .1)
	Abias_new = Abias  - (problem2e(dataset, Aw1, Aw2, Abias, z)  * .1)

	#print (Aw1_new, Aw2_new, Abias_new)

	Bw1_new = Bw1 - (problem2e(dataset, Bw1, Bw2, Bbias, x) * .1)
	Bw2_new = Bw2  - (problem2e(dataset, Bw1, Bw2, Bbias, y)  * .1)
	Bbias_new = Bbias  - (problem2e(dataset, Bw1, Bw2, Bbias, z)  * .1)

	print("Mean Squared Error for First Set of Weights: ")
	print("Old Weights: {} {} {} " .format (Aw1, Aw2, Abias))
	print("New Weights: {} {} {} " .format (Aw1_new, Aw2_new, Abias)) 

	print("Mean Squared Error for Second Set of Weights: ")
	print("Old Weights: {} {} {} " .format (Bw1, Bw2, Bbias))
	print("New Weights: {} {} {} " .format (Bw1_new, Bw2_new, Bbias)) 

	plot2e(dataset, Aw1, Aw2, Abias, Aw1_new, Aw2_new, Abias_new) 
	plot2e(dataset, Bw1, Bw2, Bbias, Bw1_new, Bw2_new, Bbias_new) 


def plot2e(dataset:list , w1: float, w2: float, bias: float, w1_new: float, w2_new: float, bias_new:float ) -> None: 

	x = []
	y1 = []
	y1_new = [] 


	for d in range (0, len(dataset)):
		x_value = (dataset[d, 1])
		x.append(x_value)
		y1.append((((-1 * w1) * x_value) - bias)/w2)
		y1_new.append((((-1 * w1_new) * x_value) - bias_new)/w2_new)

	plt.figure(1)
	colmap = {0: 'x', 1: 'v'}
	for d in range(0,len(dataset)):
		plt.scatter(dataset[d, 1], dataset[d,2], s=7, marker = colmap[dataset[d,0]])

	plt.plot(x, y1, 'g-', linewidth=2, markersize=12)
	plt.plot(x, y1_new, 'r-', linewidth=2, markersize=12)

	plt.title("Excercise 2. D")
	plt.xlabel('Petal Length')
	plt.ylabel('Petal Width')

	plt.show()


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

	#problem2b(dataset)
	callProblem2e(dataset)

main()









