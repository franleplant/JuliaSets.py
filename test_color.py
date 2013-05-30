import unittest
import color
import math


# Testing for Success
class KnownValues(unittest.TestCase):

	k = 10
	fase = 0
	h = [	round(0.0*k/360, 12),
			round(1.0*k/360, 12),
			round(5.0*k/360, 12),
			round(10.0*k/360, 12),
			round(15.0*k/360, 12),
			round(30.0*k/360, 12),
			round( math.fmod(60.0*k,360)/360, 12)	]



	knownValues = ( 	(0,  (h[0], 1,1), (255, 0,   0  )), 
						(1,  (h[1], 1,1), (255, 43,  0  )),
						(5,  (h[2], 1,1), (255, 213, 0  )),
						(10, (h[3], 1,1), (85,  255, 0  )),
						(15, (h[4], 1,1), (0,   255, 128)),
						(30, (h[5], 1,1), (255, 0,   255)),
						(60, (h[6], 1,1), (0,   0,   255)) 	)



	def test_hsv_KnownValues(self):
		""" color.hsv() should give known output for known input"""
		for integer, hsv_color, rgb_color in self.knownValues:
			output = color.hsv(integer, k=self.k, fase=self.fase)
			self.assertEqual(hsv_color, output)

	def test_intToRgb_knownValues(self):
		""" color.intToRgb() should give known output for known input """
		for integer, hsv_color, rgb_color in self.knownValues:
			output = color.intToRgb(integer,k=self.k, fase=self.fase)
			self.assertEqual(rgb_color, output)





# Testing Failure
class BadInput(unittest.TestCase):
	def test_i_NotInteger_intToRgb(self):
		""" color.intToRgb() should fail with non integer i """
		self.assertRaises(color.NotIntegerError, color.intToRgb, 1.5, 1, 0)

	def test_i_Negative_intToRgb(self):
		""" color.intToRgb() should fail with negative i """
		self.assertRaises(color.OutOfRangeError, color.intToRgb, -5, 1, 0)

	def test_k_NotInteger_intToRgb(self):
		""" color.intToRgb() should fail with not integer k """
		self.assertRaises(color.NotIntegerError, color.intToRgb, 1, 0.1, 0)

	def test_k_Negative_intToRgb(self):
		""" color.intToRgb() should fail with negative k """
		self.assertRaises(color.OutOfRangeError, color.intToRgb, 1, -5, 0)

	def test_fase_NotInteger_intToRgb(self):
		""" color.intToRgb() should fail with not integer fase """
		self.assertRaises(color.NotIntegerError, color.intToRgb, 1, 1, 10.5)

	def test_fase_Negative_intToRgb(self):
		""" color.intToRgb() should fail with negative fase """
		self.assertRaises(color.OutOfRangeError, color.intToRgb, 1, 1, -10)

	def test_fase_Big_intToRgb(self):
		""" color.intToRgb() should fail with negative fase > 360 """
		self.assertRaises(color.OutOfRangeError, color.intToRgb, 1, 1, 361)




	def test_i_NotInteger_hsv(self):
		""" color.intToRgb() should fail with non integer i """
		self.assertRaises(color.NotIntegerError, color.hsv, 1.5, 1, 0)

	def test_i_Negative_hsv(self):
		""" color.intToRgb() should fail with negative i """
		self.assertRaises(color.OutOfRangeError, color.hsv, -5, 1, 0)

	def test_k_NotInteger_hsv(self):
		""" color.hsv() should fail with not integer k """
		self.assertRaises(color.NotIntegerError, color.hsv, 1, 0.1, 0)

	def test_k_Negative_hsv(self):
		""" color.hsv() should fail with negative k """
		self.assertRaises(color.OutOfRangeError, color.hsv, 1, -5, 0)

	def test_fase_NotInteger_hsv(self):
		""" color.hsv() should fail with not integer fase """
		self.assertRaises(color.NotIntegerError, color.hsv, 1, 1, 10.5)

	def test_fase_Negative_hsv(self):
		""" color.hsv() should fail with negative fase """
		self.assertRaises(color.OutOfRangeError, color.hsv, 1, 1, -10)

	def test_fase_Big_hsv(self):
		""" color.hsv() should fail with negative fase > 360 """
		self.assertRaises(color.OutOfRangeError, color.hsv, 1, 1, 361)

	

# Testing for Sanity

## aca van a venir cosas de Color



if __name__ == "__main__":
	unittest.main()