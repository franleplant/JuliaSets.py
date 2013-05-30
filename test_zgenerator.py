import unittest
import zgenerator
import numpy
from numpy import matrix as M


# Testing for Success
class KnownValues(unittest.TestCase):

	m2 = M([[-1.5 + 1.5j, 1.5 + 1.5j], [-1.5 + -1.5j, 1.5 -1.5j]])
	m3 = M([[-1.5 + 1.5j, 0 + 1.5j, 1.5 + 1.5j], [-1.5 +0j, 0 + 0j, 1.5 + 0j], [-1.5 - 1.5j, 0 - 1.5j, 1.5 - 1.5j]])

	knownValues = ( (2, m2), 
					(3, m3)	)


	def testKnownValues(self):
		""" zgenerator.plane() should should give known output for known input """
		for n, result in self.knownValues:
			output = zgenerator.plane(n)
			notError = (result == output).all()
			self.assertEqual(True, notError)


# Testing Failure
class BadInput(unittest.TestCase):

	def test_n_NotInteger(self):
		""" zgenerator.plane() should recive an integer """
		self.assertRaises(zgenerator.NotIntegerError, zgenerator.plane, 5.0)

	def test_n_TooShort(self):
		""" zgenerator.plane() should recive an integer > 1 """
		self.assertRaises(zgenerator.OutOfRangeError, zgenerator.plane, 1)



# Testing for Sanity

## aca van a venir cosas de Color



if __name__ == "__main__":
	unittest.main()