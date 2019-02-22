import json
import math
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
from numba import njit
import openpyxl as opx
from os import remove 
import scipy.stats as ss

test = np.histogram([1,2,3,4,5,6,7,8,7,6,22,3,5,3,4,1,2,5,6],density=True,bins=10)
print(test)
plt.hist([-5,-4,-3,-2,-2,-1,-1,-1,0,0,0,0,1,1,1,2,2,3,4],bins=10,align='mid',density=True)
plt.show()