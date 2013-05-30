import numpy
import color
import math
import cmath


class CalcError(Exception): pass
class NotComplexError(CalcError): pass
class NotIntegerError(CalcError): pass
class OutOfRangeError(CalcError): pass




def it(Z,c,max_iteration):
	""" This function takes a Complex matrix
		and returns a Matrix filled with number of iterations
		taken by every complex number to escape (|z|>2)
	 """

	if not numpy.iscomplexobj(c):
		raise NotComplexError, "c parameter must be complex"

	if not numpy.iscomplexobj(Z):
		raise NotComplexError, "The Z matrix (complex plane) must be complex"

	if max_iteration == 0 :
		raise OutOfRangeError, "Number of iterations should be a positive Integer and not 0"

	if max_iteration < 0 :
		raise OutOfRangeError, "Number of iterations should be a positive Integer and not negative"

	if not type(max_iteration) is int:
		raise NotIntegerError, "Number of iterations should be a positive Integer and not float"

	

	# just to keep the dimensions
	I = Z.copy()
	C = Z.copy()
	C.fill(c)
	W = Z.getA()


	i = 0

	zn = 0 + 0j
	for z in numpy.nditer(I, op_flags=['readwrite']):
		i = max_iteration
		zn = z[()]

		for j in range(-1,max_iteration):
			if abs(zn) > 2: 
				i = j +1
				break

			#zn = zn**3 + c
			#print zn.real
			zn = cmath.exp(zn**3) + c

		#print z[...]

		# hacer aca la trans color(i)
		z[...] = i*10


	return  (I.real).astype(int)





