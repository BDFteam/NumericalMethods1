# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:38:21 2021

"""

import math
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import optimize

def main():
    # false_position()
    bisection_method()
    # modified_false_position()

def f(x):
    result = 1/x - np.log(x) + np.log(2)
    return result

def plot():
    x = 0.1
    i = 0
    qq = np.empty(199)
    qr = np.empty(199)
    while x <= 20 :
        qq[i] = f(x)
        qr[i] = x
        x += 0.1
        i += 1
    plt.grid(linestyle=':',linewidth=1.5)
    plt.plot(qr,qq)
   
def false_position():
    left_boundry = 1
    right_boundry = 5
    iterations = 0

    left_boundry_array = np.empty(100)          # 100 bigger than max iteration
    right_boundry_array = np.empty(100)
    left_boundry_array[0] = left_boundry
    right_boundry_array[0] = right_boundry
    equals_zero = False
    width_interval_reached = False
    max_iterations_reached = False
    max_iterations = 50
    minimum_witdh = 0.000001
    acceptable_error = 0.00000001
    c = 0.0
    
    while (not equals_zero) and (not width_interval_reached) and (not max_iterations_reached):
        iterations += 1
        c = (left_boundry * f(right_boundry) - right_boundry * f(left_boundry))/(f(right_boundry) - f(left_boundry))
        
        if abs(f(c)) < acceptable_error:
            equals_zero = True
        elif f(c) * f(left_boundry) > 0:
            left_boundry = c          
        else:
            right_boundry = c
        left_boundry_array[iterations] = left_boundry
        right_boundry_array[iterations] = right_boundry
        if iterations == max_iterations :
            max_iterations_reached = True
        if right_boundry - left_boundry < minimum_witdh:
            width_interval_reached = True
    root = c
    print(f"{root=}\n{equals_zero=}\n{width_interval_reached=}\n{max_iterations_reached=}\n{left_boundry=}\n{right_boundry=}\n{iterations=}")
    return root

def bisection_method():
    left_boundry = 1
    right_boundry = 5
    iterations = 0

    left_boundry_array = np.empty(100)          # 100 bigger than max iteration
    right_boundry_array = np.empty(100)
    left_boundry_array[0] = left_boundry
    right_boundry_array[0] = right_boundry
    equals_zero = False
    width_interval = False
    max_iterations_reached = False
    max_iterations = 50
    width_interval = 0.00000001
    acceptable_error = 0.00000001
    c = 0.0

    while (not equals_zero) and (not width_interval) and (not max_iterations_reached):
        iterations += 1
        c = left_boundry + (right_boundry - left_boundry)/2
        
        if abs(f(c)) < acceptable_error:
            equals_zero = True
        elif np.sign(f(c)) == np.sign(f(left_boundry)):
            left_boundry = c          
        else:
            right_boundry = c
        
        left_boundry_array[iterations] = left_boundry
        right_boundry_array[iterations] = right_boundry
        
        if iterations == max_iterations :
            max_iterations_reached = True
        
        if right_boundry - left_boundry < width_interval:
            width_interval = True
    
    root = c
    print(f"{root=}\n{equals_zero=}\n{width_interval=}\n{max_iterations_reached=}\n{left_boundry=}\n{right_boundry=}\n{iterations=}")
    return root

def modified_false_position():
    left_boundry = 1
    right_boundry = 5
    iteration = 0

    counter_left_boundry_used = 0
    counter_right_boundry_used = 0

    left_boundry_array = np.empty(100)          # 100 bigger than max iteration
    right_boundry_array = np.empty(100)
    left_boundry_array[0] = left_boundry
    right_boundry_array[0] = right_boundry

    equals_zero = False
    width_interval_reached = False
    max_iterations_reached = False
    max_iterations = 50
    width_interval = 0.000001
    acceptable_error = 0.00000001
    c = 0.0

    while (not equals_zero) and (not width_interval_reached) and (not max_iterations_reached):
        iteration += 1
        if counter_left_boundry_used == 2 or counter_right_boundry_used == 2 :
            if f(left_boundry)*f(right_boundry) > 0:
              c = (left_boundry * f(right_boundry) - 2 * right_boundry * f(left_boundry))/(f(right_boundry) - 2 * f(left_boundry))
            else:
              c = (2 * left_boundry * f(right_boundry) - right_boundry * f(left_boundry))/(2 * f(right_boundry) - f(left_boundry))
        else :
            c = (left_boundry * f(right_boundry) - right_boundry * f(left_boundry))/(f(right_boundry) - f(left_boundry))

        if abs(f(c)) < acceptable_error:
            equals_zero = True
        elif f(c) * f(left_boundry) > 0 :
            left_boundry = c
            counter_right_boundry_used += 1
            counter_left_boundry_used = 0
        else:
            right_boundry = c
            counter_left_boundry_used += 1
            counter_right_boundry_used = 0
        
        left_boundry_array[iteration] = left_boundry
        right_boundry_array[iteration] = right_boundry
        if iteration == max_iterations :
            max_iterations_reached = True
        
        if right_boundry - left_boundry < width_interval:
            width_interval_reached = True
        
    root = c
    print(f"{root=}\n{equals_zero=}\n{width_interval_reached=}\n{max_iterations_reached=}\n{left_boundry=}\n{right_boundry=}\n{iteration=}")
    return root
       
if __name__ == "__main__":
    main()