import unittest
import calc
import numpy
from numpy import matrix as M


# Testing for Success
class KnownValues(unittest.TestCase):

	c = 0 + 0j

	max_iteration = 10

	Z = M([ [0 + 0j, 1 + 0j, 0 + 1j], [.5 + .5j, -.5 + .5j, -.5 - .5j], [1.5 + 1.5j, 1.3 - 1.3j, 1.2 + 0.5j] ])

	I = M([ [max_iteration, max_iteration, max_iteration], [max_iteration, max_iteration, max_iteration], [ 0, 1, 2] ])


	def testItKnownValues(self):
		""" calc.it() should give known output for known input"""
		output = calc.it(self.Z,self.c,self.max_iteration)
		notError = (self.I == output).all()
		self.assertEqual(True, notError)


class KnownValuesConstant(unittest.TestCase):

	c = 1 + 0j

	max_iteration = 10

	Z = M([[0 + 0j]])

	I = M([[3]])

	def testItConstantAdd(self):
		""" calc.it() should add c on every iteration """

		output = calc.it(self.Z,self.c,self.max_iteration)
		notError = (self.I == output).all()
		self.assertEqual(True, notError)

# Testing Failure
class BadInput(unittest.TestCase):
	def test_Z_NotComplex(self):
		""" calc.it() should fail with non complex Z """
		self.assertRaises(calc.NotComplexError, calc.it, M([[1]]), 0 + 0j, 10)

	def test_C_NotComplex(self):
		""" calc.it() should fail with non complex c """
		self.assertRaises(calc.NotComplexError, calc.it, M([[1 + 1j]]), 1, 10)

	def test_Max_Iteration_NotInteger(self):
		""" calc.it() should fail with non integer max_iteration """
		self.assertRaises(calc.NotIntegerError, calc.it, M([[1 + 1j]]), 0 + 0j, 10.5)

	def test_Max_Iteration_Negative(self):
		""" calc.it() should fail with negative max_iteration """
		self.assertRaises(calc.OutOfRangeError, calc.it, M([[1 + 1j]]), 0 + 0j, -10)

	def test_Max_Iteration_NotZero(self):
		""" calc.it() should fail with zero max_iteration """
		self.assertRaises(calc.OutOfRangeError, calc.it, M([[1 + 1j]]), 0 + 0j, 0)


# Testing for Sanity

## aca van a venir cosas de Color



if __name__ == "__main__":
	unittest.main()