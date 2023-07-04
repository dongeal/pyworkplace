import numpy as np
n=int(input('숫자를 입력하시오: '))

carray = np.zeros((n,3))

for i in range(0,n):
    carray[i,0] = i+1

print(carray) 