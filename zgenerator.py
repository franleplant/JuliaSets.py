from numpy import matrix as M
import numpy

class ZgeneratorError(Exception): pass
class NotIntegerError(ZgeneratorError): pass
class OutOfRangeError(ZgeneratorError): pass


def plane(n):
	""" commments """
	if not n > 1:
		raise OutOfRangeError, "zgenerator.plane(n): n should be > 1"

	if not type(n) is int:
		raise NotIntegerError, "zgenerator.plane(n): n should be integer"


	r = 3.0
	res = float(n-1)

	v = numpy.zeros(n**2).reshape(n,n)
	v = v.astype(complex)

	for row in range(n):
		i = float(row)
		im =   (r/2 - r*i/res)

		for col in range(n):			
			j = float(col)			
			re =  (-r/2 + r*j/res)
			v[i][j] = re + im*1j


	m = M(v)

	return m

	