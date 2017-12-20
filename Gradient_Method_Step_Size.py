# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 13:41:07 2017

@author: Paulina
"""

import numpy as np
import matplotlib.pyplot as plt

def descent(multipler):
    gamma = multipler # Step size multipler
    cur_x = -30 # The algoritm starts at x = -5
    precision = 0.00001
    previous_step_size = 2*precision
    i = 1
    while previous_step_size > precision:
        prev_x = cur_x
        cur_x += -gamma * df(prev_x)
        previous_step_size = abs(cur_x - prev_x)
        i += 1
    # print "The local minimum accours at %f" %cur_x
    # print "Number of iterations:", i
    return i

gammas = []
iterations = []

for gamma in np.arange(0.005,1,0.0005):
    i = descent(gamma)
    gammas.append(gamma)
    iterations.append(i)
    
print (gammas, len(gammas))
print (iterations, len(iterations))

plt.plot(gammas, iterations)
plt.show()