# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 18:02:53 2017

@author: Paulina
"""

import numpy as np
import matplotlib.pyplot as plt

#Numerical derivative parameters
x0 = 0.002
xmax = 0.008
delta = 0.00001

#Geometric and heat transfer parameters
alpha_1 = 1500      #[W/m2K]
alpha_2 = 12        #[W/m2K]
lambda_1 = 120      #[W/mK]
lambda_2 = 0.2      #[W/mK]
d1 = 0.02           #[m]
d2 = 0.024          #[m] 

#Thermal resistance calculations
def f(x):
    A =1/(alpha_1*d1)
    B =np.log(d2/d1)/(2*lambda_1)
    C =np.log((d2+2*x)/d2)/(2*lambda_2)
    D =1/(alpha_2*(d2+2*x))
    return A+B+C+D

#Thermal resistance derivative
def df(x):
    df = (f(x+delta)-f(x-delta))/(2*delta)
    return df

#Gradient method parameters
cur_x = d1 #The algorithm starts at inner diameter
gamma = 0.0001 #Step size multiplier
precision = 0.000001
previous_step_size =2*precision

#Gradient method algorithm
while previous_step_size > precision:
    prev_x = cur_x
    print (cur_x)
    cur_x += -gamma *df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    
print("Critical thickness: %f [m]" % cur_x)

#Ploting section
args = []
values = []
derivatives = []

for x in np.arange(x0,xmax,delta):
    args.append(x)
    values.append(f(x))
    derivatives.append(df(x))
    
plt.plot(args, values)
plt.xlabel("Insulation thickness [mm]")
plt.ylabel("Thermal resistance [mm]")
plt.grid()