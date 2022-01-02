import numpy as np
N,M = map(int,input().split())
A = np.array([input().split() for _ in range(N)], int)
print(A.mean(axis=1))
print(A.var(axis=0))
print(A.std().round(11))
