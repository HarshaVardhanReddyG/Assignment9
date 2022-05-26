#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt 
import math
print(math.e)
def f(y): 
    if (y<=0).all():
        return 1/math.sqrt(2*math.pi)*((math.e)**-(((y-1)**2)/2))
    else :
        return  1/math.sqrt(2*math.pi)*((math.e)**-(((y+1)**2)/2))
    return 0.0 


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True


y= np.linspace(0, 3, 100)

plt.plot(y, f(y), color='red')

plt.show()
