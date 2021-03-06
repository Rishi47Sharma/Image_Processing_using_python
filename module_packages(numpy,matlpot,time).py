# -*- coding: utf-8 -*-
"""Module_Packages(numpy,matlpot,time).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k9YtNU13GsfSwfg29nRcNzQd1HPPOi7Y
"""

import numpy as np
import matplotlib.pyplot as plt
import time as t

a=np.array([2,5,1,7,6,93])
print(a)
print(type(a))
print(np.__doc__)

b=a.reshape(3,2)
print(b)#to arrange elemet in verious dimension
print(b.shape)
r=np.arange(16)
print(r)
print (np.linspace(0,10,7))

print(np.zeros(4))
print(np.ones(4))
plt.plot(a)

"""Diagonals"""

print(np.eye(2))
t=np.diag([45,33,56,78])
print(t)

"""Indexing and slicing"""

q=r.reshape(4,4)
print(q[0:3,0:4])
print(q)

"""Example:"""

a=int(input())
b=np.arange((a*a))
d=b.reshape(a,a)
print(d)

print("A =",d[0:a//2,0:a//2])
print("B =",d[0:a//2,a//2:a])
print("C =",d[a//2:a,0:a//2])
print("D =",d[a//2:a,a//2:a])

a=int(input())
b=np.arange((a*a))
d=b.reshape(a,a)
print(d)
print(d[0:5:2,0:5:2])#3rd value indicate the difference

p=np.ones(5)
q=np.zeros(2)
c=np.concatenate([p,q])
print(c)
a=np.random.random(3)
print(a)

"""Transpose Of a matrix"""

a =(np.arange(11)+1).reshape(5,2)
b=a.T
print(a)
print(b)

"""Concatenation of list and element of array"""

a=[12,32,43]
b=[23,45,56]
c=a+b
print(c)
d=np.array([12,32,43])
e=np.array([23,45,56])
f=d+e
g=e-d
h=e>f
i=e*b
k=np.dot(e,f)
print(f,g,h,i,k)

a=(np.arange(25,50)).reshape(5,5)
b=(np.arange(25)).reshape(5,5)
c=np.dot(a,b) #dot multiplication of matrix
d=a*b
print(c)
print(d)

"""time module"""

print(t.perf_counter())
print(t.time())
print(t.ctime())

n =50 
a=np.arange(n*n)+1
a=a.reshape(n,n)
b=a.T
c=np.zeros((n,n))
d=t.time()
for i in range(n):
  for j in range(n):
    for k in range(n):
      c[i][j]+=a[i][k]*b[k][j]
print(t.time()-d)