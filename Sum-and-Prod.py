import numpy

n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
summ= numpy.sum(array,axis=0)
print (numpy.prod(summ))
