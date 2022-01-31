import numpy as np
m=int(input())
n=int(input())



a=(np.random.default_rng()).integers(50,100,[m,n])
print("matrix without sorting:")
print('\n',a)
temp=[]
print("\nmatrix row wise sorted:")
for i in range(m) :
  for j in range(n):
    temp.append(a[i][j])
temp=sorted(temp)
r=np.reshape(temp,(m,n))
print("\n",r)
print("\nmatrix column wise sorted:")
temp_1=[]
for i in range(n):
  for j in range(m):
    
    temp_1.append(a[j][i])
temp_1=sorted(temp_1)
c=np.reshape(temp_1,(m,n))
print('\n',c)

