# -*- coding: utf-8 -*-
"""P5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1esyjUuq1zCdLTk4RTSwrYkWSamRS9bCw
"""

import numpy as np

def division(n,a,b):
  array=np.arange(n)
  array_a=[]
  array_b=[]
  #print(array)
  for i in array:
    if (i%a==0):
      array_a.append(i)
  #print(array_a)
  for i in array_a:
    if(i%b!=0):
      array_b.append(i)
  
  return array_b

print("Enter n ",end=":")
n=int(input())
print("Enter a ",end=":")
a=int(input())
print("Enter b ",end=":")
b=int(input())

print(division(n,a,b))