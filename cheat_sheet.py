# pylint: skip-file

from functools import cmp_to_key
from itertools import product
# the same as:
def productor(lists):
    if not lists:
        yield []
    else:
        for element in lists[0]:
            for rest in productor(lists[1:]):
                yield [element] + rest
lists = [[1,2,3],[1,2]]
print(list(productor(lists)))

from collections import deque
from math import inf,sqrt,ceil,comb
from sys import exit,stdin
one = 1
pai = 3.1415926535
print(f'{pai:.3f}')
#3.142
print('%.3f' % pai)
#3.142
def cmp(a,b):
    if a > b:
        return -1
    else:
        return 1
print(sorted([one,pai],key=cmp_to_key(cmp)))
#[3.1415926535, 1]

#质数表
n = 10
z = [None,0]+[1]*(n-1)
for i in range(1,int(n/2)+1):
    if z[i] == 1:
        for j in range(2*i,n+1,i):
            z[j] = 0
print(z)



#uesless
a = [1]
for i in a:
    a = [1,2]
    print(i)
#1

ii = list(range(10))
for i in ii:
    ii.remove(i)
print(ii)
#[1, 3, 5, 7, 9]

l = [[0,0,0]]*5
l[0][0] = 1
print(l)
#[[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]

#useful
a = [1]
for i in a:
    if i < 2:
        a.append(2)
    print(i)
#1
#2

ii = list(range(10))
iic = ii[:]
for i in ii:
    iic.remove(i)
print(iic)
#[]

l = [[0,0,0] for i in range(5)]
l[0][0] = 1
print(l)
#[[1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
