# -*- coding: utf-8 -*-
"""Dictionary_Docstring_Class.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OBPmdEiyhmTopwLADNw64mUSTyIuVkKo
"""

a={ 1:5,'a':["hi","my","name"],'z':123}
print(a['a'])

for i in a:
  print(i)
for i in a.keys():
  print(i)
for i in a.values():
  print(i)
for i in a.items():
  print(i)

"""Doctstring:Describe the function in one string
function.__doc__
"""

def xyz(a):
  'this is xyz function'
  return a*a

print(xyz.__doc__)
help(xyz)

class a:
  x = None #public
  _y=None #protected
  __z=None #Private
  def __init__(self,x,y,z):
    self.x=x
    self._y=y
    self.__z=z
  def _proctected_prod(self): 
    return self.x*self._y*self.__z
  def pub_prod(self):
     return self.x*self._y*self.__z
   
  def __private_prod(self):
    return self.x*self._y*self.__z

b = a(2,3,4)
print(b.x)
print(b._y)
#print(b.__z)

var1=b._proctected_prod()
var2=b.pub_prod()
#var3=b.__private_prod()
print(var1,var2,end=" ")