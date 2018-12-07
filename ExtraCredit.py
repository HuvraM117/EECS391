#Huvra Mehta [hsm20]

# Import necessary libraries
import random
from copy import deepcopy
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import csv


sepal_length = []
sepal_width  = []
petal_length = []
petal_width  = []
species_data = []

def data() -> None:

    with open('irisdata.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sepal_width.append(float(row['sepal_width']))
            sepal_length.append(float(row['sepal_length']))
            petal_width.append(float(row['petal_width']))
            petal_length.append(float(row['petal_length']))
            species_data.append(row['species'])

def kmeans(K: int, dataset: list) -> float:

    #stop it if it goes on for too long 
    max_iter = 1000
    i = 0

    idx = np.random.randint(10, size=K)
    centers = dataset[idx,:]

    print(centers)

    #plot intial plot
    colmap = {0: 'r', 1: 'g', 2: 'b'}
    for d in range(0,len(dataset)):
        plt.scatter(dataset[d, 1], dataset[d,2], s=7, color = colmap[dataset[d, 0]])

    for c in range(0, len(centers)):
        plt.scatter(centers[c,1], centers[c,2], marker='*', c='g', s=150)
    plt.show()

    #keep track of when to print middle graph 
    count = 0

    cont = True 

    while (cont) and (i < max_iter):
        old_centers = deepcopy(centers)
        print(centers)
        
        i += 1 #we are making an attempt 

        for d in range(0,len(dataset)):
            old_dist = dataset[d, 1]

            for k in range(0,len(centers)):

                dx = dataset[d, 1]
                dy = dataset[d, 2]
                cx = centers[k, 1]
                cy = centers[k, 2]

                dist = math.sqrt(((dx - cx)**2) + ((dy - cy)**2))

                if (dist < old_dist):
                    old_dist = dist
                    dataset[d, 0] = k #since it starts at 0 i need it to go from 1, 2, 3

        
        #for each of the means find all the data points with the right indicator (1,2)
        for k in range (0, len(centers)):
            x_value = 0
            y_value = 0
            counter = 0 
            for d in range (0, len(dataset)):
                if (dataset[d,0] == k):
                    x_value += dataset[d, 1]
                    y_value += dataset[d, 2]
                    counter = counter + 1

            x_value = x_value/float(counter)
            y_value = y_value/float(counter)

            centers[k, 1] = x_value
            centers[k, 2] = y_value

        if np.array_equal(centers, old_centers):
            cont = False

        print(dataset)
        count += 1
        print(count)

        #plot middle plot
        if (count == 4):
            colmap = {0: 'r', 1: 'g', 2: 'b'}
            for d in range(0,len(dataset)):
                plt.scatter(dataset[d, 1], dataset[d,2], s=7, color = colmap[dataset[d, 0]])

            for c in range(0, len(centers)):
                plt.scatter(centers[c,1], centers[c,2], marker='*', c='g', s=150)
            plt.show()

    #plot final plot
    colmap = {0: 'r', 1: 'g', 2: 'b'}
    for d in range(0,len(dataset)):
        plt.scatter(dataset[d, 1], dataset[d,2], s=7, color = colmap[dataset[d, 0]])

    for c in range(0, len(centers)):
        plt.scatter(centers[c,1], centers[c,2], marker='*', c='g', s=150)
    plt.show()

def main():
    #create dataset 
    data()

    cluster = [0] * len(petal_length)
    df = pd.DataFrame({
        'x': petal_length,
        'y': petal_width,
        'c': cluster
    })

    # Change dataframe to numpy matrix
    dataset = df.values[:, 0:4]

    #kmeans(2,dataset)
    kmeans(3,dataset)

main()
