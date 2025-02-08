
import array
from array import *

import array


for i in range(4):
    for j in range(4):
        print("#", end=" ")
    print()

for i in range(1,5):
    for j in range(i,5):
        print(j, end=" ")

    print()
for num in range (2,1000):
    is_prime = True
    for i in range (2, int(num**0.5)+1):
        if num%i==0:
            is_prime= False
            break
    if is_prime:
        print(num, end=" ")


