import numpy as np

A=np.array([[5,2,0],[0,1,4],[1,-4,1]])
x=np.array([[1],[2],[0]])

b=np.dot(A,x)
print(b)