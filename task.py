import numpy as np
# using slicing operator
# task is to to extract sub arrays from 2d and 3d arrays
# operations on 1d array
array_1=[1,2,3,4,5,6,7,8,9]
np.array(array_1)
z=(array_1[2:8:2])
# print(z)
# #negative slicing
x=(array_1[::-1])
print(x)

#2d arrays
array_2=[[1,2,3,4],[7,8,9,10]]
array_2=np.array(array_2)
z=(array_2[1,1:2])
print(z)
#extract an number from an 2d array
x=(array_2[1:4,1:4])
print(x)
condition = array_2 > 3
selected_elements = array_2[condition]
print(selected_elements)

# 3d array

array_3 = np.array([[[1, 2],
                    [3, 4]],
                    [[5, 6],
                    [7, 8]]])

np.array(array_3)
x=array_3[0:1,0:1,0:1]
print(x)

z=array_3[0,1,1]

print(z)

subarray = array_3[1:2, 1:2, 0:2]

print(subarray)


