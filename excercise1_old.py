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
    FalsePosition()
    #BisectionMethod()
    # ModifiedFalsePosition()
    return

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
   
def FalsePosition():
    a = 1
    b = 5
    k = 0
    ak = np.empty(100)          # 100 bigger than max iteration
    bk = np.empty(100)
    ak[0] = a
    bk[0] = b
    equalszero = False
    widthinterval = False
    maxiterations = False
    maxiterationsnum = 50
    widthintervalnum = 0.000001
    acceptableerror = 0.00000001
    while equalszero == False and widthinterval == False and maxiterations == False:
        k += 1
        c = (a * f(b) - b * f(a))/(f(b) - f(a))
        if abs(f(c)) < acceptableerror:
            equalszero = True
        elif f(c) * f(a) > 0 :
            a = c          
        else:
            b = c
        ak[k] = a
        bk[k] = b
        if k == maxiterationsnum :
            maxiterations = True
        if b - a < widthintervalnum:
            widthinterval = True
    root = c
    print(root, equalszero, widthinterval, maxiterations, a, b, k)
    return root

def BisectionMethod():
    a = 1
    b = 5
    k = 0
    ak = np.empty(100)          # 100 bigger than max iteration
    bk = np.empty(100)
    ak[0] = a
    bk[0] = b
    equalszero = False
    widthinterval = False
    maxiterations = False
    maxiterationsnum = 50
    widthintervalnum = 0.00000001
    acceptableerror = 0.00000001
    while equalszero == False and widthinterval == False and maxiterations == False:
        k += 1
        c = a + (b - a)/2
        if abs(f(c)) < acceptableerror:
            equalszero = True
        elif np.sign(f(c)) == np.sign(f(a)):
            a = c          
        else:
            b = c
        ak[k] = a
        bk[k] = b
        if k == maxiterationsnum :
            maxiterations = True
        if b - a < widthintervalnum:
            widthinterval = True
    root = c
    print(root, equalszero, widthinterval, maxiterations, a, b, k)
    return root

def ModifiedFalsePosition():
    a = 1
    b = 5
    k = 0
    qa = 0
    qb = 0
    ak = np.empty(100)          # 100 bigger than max iteration
    bk = np.empty(100)
    ak[0] = a
    bk[0] = b
    equalszero = False
    widthinterval = False
    maxiterations = False
    maxiterationsnum = 50
    widthintervalnum = 0.000001
    acceptableerror = 0.00000001
    while equalszero == False and widthinterval == False and maxiterations == False:
        k += 1
        if qa == 2 or qb == 2 :
            if f(a)*f(b) > 0:
              c = (a * f(b) - 2 * b * f(a))/(f(b) - 2 * f(a))
            else:
              c = (2 * a * f(b) - b * f(a))/(2 * f(b) - f(a))
        else :
            c = (a * f(b) - b * f(a))/(f(b) - f(a))
        if abs(f(c)) < acceptableerror:
            equalszero = True
        elif f(c) * f(a) > 0 :
            a = c
            qb = 0
            qa += 1
        else:
            b = c
            qa = 0
            qb += 1
        ak[k] = a
        bk[k] = b
        if k == maxiterationsnum :
            maxiterations = True
        if b - a < widthintervalnum:
            widthinterval = True
    root = c
    print(root, equalszero, widthinterval, maxiterations, a, b, k)
    return root
       
if __name__ == "__main__":
    main()