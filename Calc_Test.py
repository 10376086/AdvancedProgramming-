import unittest
from calc import add, subtract

class CalculatorTest (unittest.TestCase):

def testAdd(self):
  self.assertEqual(4, add(2,2))
  self.assertEqual(5, add(2,3))
  self.assertEqual(8.3, add(2.8, 5.5))
	
def testSubtract(self):
 
  self.assertEqual(0, add(2,2))
  self.assertEqual(-1, add(2,3))
  self.assertEqual(4.5, add(10, 5.5))
