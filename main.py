import calc
import color
import zgenerator
# import scipy.misc.pilutil as smp
import matplotlib.pyplot as plt
from scipy import misc
import numpy

n = 500

Z = zgenerator.plane(n)
IMG = calc.it(Z, 0.279 + 0j, 100)

#l = misc.lena()

#print IMG[0][1]

A = numpy.zeros(n**2*3).reshape(n,n,3)

for i in range(n):
	for j in range(n):
		k = IMG[i,j]
		#print color.intToRgb(k,3,0)
		A[i][j] = color.intToRgb(k,1,180)


#print A
plt.figure()
plt.imshow(A)
plt.show()

#plt.imshow(l, cmap=plt.cm.gray)


# plt.imshow(I, cmap=plt.cm.gray)

