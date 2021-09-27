# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:37:48 2021

@author: Maumo
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import optimize

def main():
    test()
   
   
def test():
    X = np.array([[0], [0], [6370], [0]])
    for i in range(30):
        F = functions(X)
        J = jacobian(X)
        H = np.linalg.solve(J, F)
        X = X - H        
    print(X)
       
       
def functions(X):
    C = 299792.458
    x = X[0,0]
    y = X[1,0]
    z = X[2,0]
    D = X[3,0]
    Fa = np.array([[0],[0],[0],[0]])
    Fa[0,0] = (x - 15600)**2 + (y - 7540)**2 + (z - 20140)**2 - (C * (0.07074 - D))**2
    Fa[1,0] = (x - 18760)**2 + (y - 2750)**2 + (z - 18610)**2 - (C * (0.07220 - D))**2
    Fa[2,0] = (x - 17610)**2 + (y - 14630)**2 + (z - 13480)**2 - (C * (0.07690 - D))**2
    Fa[3,0] = (x - 19170)**2 + (y - 610)**2 + (z - 18390)**2 - (C * (0.07242 - D))**2
    return Fa

def jacobian(X):
    Ja = np.zeros((4,4))
    C = 299792.458
    x = X[0,0]
    y = X[1,0]
    z = X[2,0]
    D = X[3,0]
    Ja[0,0] = 2 * (x - 15600)
    Ja[1,0] = 2 * (x - 18760)
    Ja[2,0] = 2 * (x - 17610)
    Ja[3,0] = 2 * (x - 19170)
   
    Ja[0,1] = 2 * (y - 7540)
    Ja[1,1] = 2 * (y - 2750)
    Ja[2,1] = 2 * (y - 14630)
    Ja[3,1] = 2 * (y - 610)
   
    Ja[0,2] = 2 * (z - 20140)
    Ja[1,2] = 2 * (z - 18610)
    Ja[2,2] = 2 * (z - 13480)
    Ja[3,2] = 2 * (z - 18390)
   
    Ja[0,3] = 2 * (C**2) * 0.07074 - 2 * (C**2) * D
    Ja[1,3] = 2 * (C**2) * 0.07220 - 2 * (C**2) * D
    Ja[2,3] = 2 * (C**2) * 0.07690 - 2 * (C**2) * D
    Ja[3,3] = 2 * (C**2) * 0.07242 - 2 * (C**2) * D
 
    return Ja
   
if __name__ == "__main__":
    main() s