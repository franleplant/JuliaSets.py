import calc
import color
import zgenerator
# import scipy.misc.pilutil as smp
import matplotlib.pyplot as plt
from scipy import misc
import numpy
import math

n = 500

Z = zgenerator.plane(n)
IMG = calc.it(Z, -0.59 + 0j, 5000)



A = numpy.zeros(n**2*3).reshape(n,n,3)

#A = numpy.zeros(n**2).reshape(n,n)

for i in range(n):
	for j in range(n):
		k = IMG[i,j]
		#print color.intToRgb(k,3,0)
		A[i][j] = color.intToRgb(k,2,120)
		#A[i][j] = k * 15

#print A

#plt.figure()
plt.imshow(A)
plt.show()



