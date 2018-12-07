#Huvra Mehta (HSM20)

#Import Necessary Libraries 
import math as math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
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


def plot1(dataset) -> None: 
	colmap = {0: 'x', 1: 'v'}
	for d in range(0,len(dataset)):
		plt.scatter(dataset[d, 1], dataset[d,2], s=7, marker = colmap[dataset[d,0]])

	plt.title("Excercise 1. A")
	plt.xlabel('Petal Length')
	plt.ylabel('Petal Width')

	plt.show()

def problem1B(x: float, y: float) -> float: 
	w1 = .4
	w2 = .7
	bias = -3.2

	z = ((w1*x) + (w2*y) + bias)

	sigmoid = 1 / (1 + math.exp(-z))

	if (sigmoid < .5):
		return 0
	else:
		return 1


def plot2(dataset:list) -> None:
	colmap = {0: 'x', 1: 'v'}
	for d in range(0,len(dataset)):
		plt.scatter(dataset[d, 1], dataset[d,2], s=7, marker = colmap[dataset[d,0]])

	w1 = .4
	w2 = .7
	bias = -3.2
	x = []
	y = [] 
	for d in range (0, len(dataset)):
		x_value = (dataset[d, 1])
		x.append(x_value)
		y.append((((-1 * w1) * x_value) - bias)/w2)

	plt.plot(x, y, 'g-', linewidth=2, markersize=12)

	plt.title("Excercise 1. C")
	plt.xlabel('Petal Length')
	plt.ylabel('Petal Width')

	plt.show()


def plot3(dataset: list) -> None: 

	ax = plt.gca(projection='3d')

	x_range = np.arange(2, 8, (6/500)) 
	y_range = np.arange(0, 3, (6/500)) 

	x_data, y_data = np.meshgrid(x_range, y_range)
	zs = np.array([problem1B(a,b) for a,b in zip(np.ravel(x_data), np.ravel(y_data))])
	z = zs.reshape(x_data.shape)

	ax.plot_surface(x_data, y_data, z)
	
	plt.title("Excercise 1. D")
	plt.xlabel('Petal Length')
	plt.ylabel('Petal Width')
	
	plt.show()


def plot4(dataset:list) -> None:

	#Group 0 
	print("Group 0: versicolor")
	print("Point: (3.3, 1.0)")
	value = problem1B(3.3, 1.0)
	print("Category: ", value)
	print("Point: (3.3, 1.0)")
	value1 = problem1B(4.4, 1.3)
	print("Category: ", value1)

	#Group 1
	print("Group 1: virginica")
	print("Point: (5.0, 1.9)")
	value2 = problem1B(5.0, 1.9)
	print("Category: ", value2)
	print("Point: (6.1, 2.5)")
	value3 = problem1B(6.1, 2.5)
	print("Category: ", value3)


	#Near the Line
	print("Near the Line")
	print("Point: (5.0, 1.7)")
	value4 = problem1B(5.0, 1.7)
	print("Category: ", value4)
	print("Point: (5.1, 1.6)")
	value5 = problem1B(5.1, 1.6)
	print("Category: ", value5)


	w1 = .4
	w2 = .7
	bias = -3.2
	x = []
	y = [] 
	for d in range (0, len(dataset)):
		x_value = (dataset[d, 1])
		x.append(x_value)
		y.append((((-1 * w1) * x_value) - bias)/w2)

	plt.plot(x, y, 'g-', linewidth=2, markersize=12)

	plt.plot(3.3, 1.0, 'rx')
	plt.plot(4.4, 1.3, 'rx')
	plt.plot(5.0, 1.9, 'gv')
	plt.plot(6.1, 2.5, 'gv')
	plt.plot(5.0, 1.7, 'bo')
	plt.plot(5.1, 1.6, 'bo')

	plt.title("Excercise 1. E")
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

	#print(dataset)

	#plot1(dataset)
	#plot2(dataset)
	#plot3(dataset)
	plot4(dataset)


main()









