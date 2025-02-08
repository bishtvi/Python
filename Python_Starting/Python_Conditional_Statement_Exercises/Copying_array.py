import numpy
from numpy import *

arr = array([1,2,3,4,5])

arr1 = arr + 5
print(arr1)

arr1 = array([1,2,3,4,5])
arr2 = array([6,5,4,8,9])

arr3 = arr1 + arr2

print(arr3)

print(concatenate([arr1,arr2]))

arr2 = arr1

print(arr2).3