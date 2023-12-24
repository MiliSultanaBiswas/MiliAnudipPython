#How to find the mwan of every numpy array in the given list  list=[np.array([3,2,8,9]),np.array([4,12,34,25,78]),np.array([23,12,67])]


#import numpy

import numpy as np

input=[np.array([3,2,8,9]),np.array([4,12,34,25,78]),np.array([23,12,67])] # list of input

output=[] # a blank array for store output

for i in range(len(input)):

    output.append(np.mean(input[i]))

print(output) #print the output of mean for array list


#------------------------------------------------------------------------------------------------------------------------
# output---
'''
[5.5, 30.6, 34.0]

'''