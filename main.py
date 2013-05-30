import calc
import color
import zgenerator
# import scipy.misc.pilutil as smp
import matplotlib.pyplot as plt
from scipy import misc

Z = zgenerator.plane(100)
IMG = calc.it(Z, 0.35 + 0j, 50)

l = misc.lena()

plt.imshow(l, cmap=plt.cm.gray)


# plt.imshow(I, cmap=plt.cm.gray)

