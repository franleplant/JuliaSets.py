import numpy
import color


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

	# n,m = Z.getA().shape

	# for i in range(n):
	# 	for j in range(m):
	# 		for it in range(max_iteration):
	# 			I[i,j] = I[i,j]**2 + c

	# 			if numpy.abs(I[i,j]) > 2:
	# 				I[i,j] = it 
	# 				break
	# 		print I[i,j]

	# print I.real
	# return  (I.real).astype(int)



	# for row in I:
	# 	i = 0
	# 	for z in row:
	# 		print row
	# 		for i in range(1, max_iteration + 1):

	# 			zn = z[...]
	# 			#print z[...]
	# 			zn = zn**2 + c
	# 			if numpy.abs(zn) > 2:
	# 				break
	# 			i += 1
				#print zn

	#print I

# 	n,m = Z.getA().shape
# #	IMG = numpy.zeros(n*m*3).reshape(n,m,3)

# 	IMG = numpy.zeros(n*m).reshape(n,m)

# 	i = max_iteration


# 	for j in range(max_iteration):
# 		W = W*W + C
# 		IMG = (numpy.abs(W) > 2)*(IMG == 0)*j
	#	IMG = (numpy.abs(W) > 2)*(IMG == [0,0,0])*color.intToRgb(j,0,0)

	# print "IMG"
	# print IMG
	# print "W"
	# print W
	# print "----"
	# return IMG

	i = 0

	zn = 0 + 0j
	for z in numpy.nditer(I, op_flags=['readwrite']):
		i = max_iteration
		zn = z[...]

		for j in range(-1,max_iteration):
			if abs(zn) > 2: 
				i = j +1
				break

			zn = zn*zn + c

		#print z[...]

		# hacer aca la trans color(i)
		z[...] = i

	#print (I.real).astype(int)

	return  (I.real).astype(int)





