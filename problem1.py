# /usr/bin/python3
# Huvra Mehta
# Homework 5 - Problem 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.special import comb

# Problem 1.b
# Plot the likliehood for n = 4, θ = 3/4. Plot must inclide y = 0. 
def likelihood():
    n, p = 4, 0.75
    k = np.arange(0, 4.5, .5)
    values = (comb(n, k) * p**k * (1-p)**(n-k))
    plt.plot(k, values, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
    plt.title("Problem 1.b: Likelihood")
    plt.ylabel("n=4, θ=3/4")
    plt.xlabel("k")
    plt.show()

# Problem 1.c
# Plot the posterior distribution of θ after each of the following coin flips:
# head (n = 1, y = 1), head(n = 2, y = 2), tail(n = 3, y = 2), head (n = 4, y = 3)
def posterior():
    p = np.arange(0, 1, .1) #theta 

    n, y = 1, 1 #number of trials & number of heads
    math = comb(n, y) * p**y * (1-p)**(n-y) * (1 + n)
    plt.plot(p, math, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)

    n, y = 2, 2 #number of trials & number of heads
    math1 = comb(n, y) * p**y * (1-p)**(n-y) * (1 + n)
    plt.plot(p, math1, color='orange', marker='o', linestyle='dashed', linewidth=2, markersize=12)

    n, y = 3, 2 #number of trials & number of heads
    math1 = comb(n, y) * p**y * (1-p)**(n-y) * (1 + n)
    plt.plot(p, math1, color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=12)

    n, y = 4, 3 #number of trials & number of heads
    math1 = comb(n, y) * p**y * (1-p)**(n-y) * (1 + n)
    plt.plot(p, math1, color='red', marker='o', linestyle='dashed', linewidth=2, markersize=12)

    plt.gca().legend(('Head = 1, Trial = 1','Head = 2, Trial = 2', 'Head = 2, Trial = 3', 'Head = 3, Trial = 4'), loc = 'upper left')
    plt.title("Problem 1.c: Posterior")
    plt.ylabel("Heads & Trials")
    plt.xlabel("Theta")
    plt.show()
    
likelihood()
posterior()

