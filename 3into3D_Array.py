'''
Write a numpy program to create a 3*3 matrix with values rangeing from 2 to 10.'''

import numpy as np   # import numpy

array=np.arange(2,11)   # creating array
print("the main array is:\n",array) #print the 1D array
matrix_arr=array.reshape(3,3) # reshape the array
print("3*3 matrix is :\n" ,matrix_arr)  # print the reshape arrat or 3*3 matrix

#---------------------------------------------------------------------
'''   output
the main array is:
 [ 2  3  4  5  6  7  8  9 10]
3*3 matrix is :
 [[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]


'''