import numpy as np

A=np.array([[2,5,4],[0,3,2],[0,0,4]])
b=np.transpose(np.array([[1,2,-2]]))
x=np.linalg.solve(A,b)
print(x)
