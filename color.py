import colorsys
import math

class ColorError(Exception): pass
class NotIntegerError(ColorError): pass
class OutOfRangeError(ColorError): pass


def hsv(i,k,fase): 
	""" comments """
	if type(i) is float:
		raise NotIntegerError, "i should be integer"

	if i < 0:
		raise OutOfRangeError, "i should be positive or zero"

	if not type(k) is int:
		raise NotIntegerError, "k should be integer"

	if k < 0:
		raise OutOfRangeError, "k should be positive or zero"

	if not type(fase) is int:
		raise NotIntegerError, "fase should be integer"

	if fase < 0:
		raise OutOfRangeError, "fase should be positive or zero"

	if fase > 360:
		raise OutOfRangeError, "fase should be <= to 360"



	x = float(i * k + fase)

	if i == 0:
		h = 0
	else:
		h = round(math.fmod(x, 360)/360, 12)

	s = 1
	v = 1

	return (h,s,v)



def intToRgb(i,k,fase): 
	""" comments """

	if type(i) is float:
		raise NotIntegerError, "i should be integer"

	if i < 0:
		raise OutOfRangeError, "i should be positive or zero"

	if type(k) is float:
		raise NotIntegerError, "k should be integer"

	if k < 0:
		raise OutOfRangeError, "k should be positive or zero"

	if type(fase) is float:
		raise NotIntegerError, "fase should be integer"

	if fase < 0:
		raise OutOfRangeError, "fase should be positive or zero"

	if fase > 360:
		raise OutOfRangeError, "fase should be <= to 360"


	h,s,v = hsv(i,k,fase)
	r,g,b = colorsys.hsv_to_rgb(h,s,v)

	# r = int(round(r*255))
	# g = int(round(g*255))
	# b = int(round(b*255))

	rgb = [r, g, b]

	return rgb