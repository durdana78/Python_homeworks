import numpy as np
A = np.random.randint(1,10,(5,3))
b = np.random.randint(1,10,(3,2))

c = np.dot(A,b)

print(c)