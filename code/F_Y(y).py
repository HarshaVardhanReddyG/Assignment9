#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt 
import math
from scipy.special import erf
def F(y): 
    if (y<=0).all():
        return (1/2)*(erf((y-1)/(2**0.5))+1)
    else :
        return  (1/2)*(erf((y+1)/(2**0.5))+1)
    return 0.0 


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True


y= np.linspace(-3, 0, 1000)

plt.plot(y, F(y), color='red')

plt.show()
