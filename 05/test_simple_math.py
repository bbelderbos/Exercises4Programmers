import unittest
from simple_math import divide, calcs

class TestModule(unittest.TestCase):

  def test_divide(self):
    self.assertEqual(divide(4,2), 2)
    self.assertEqual(divide(4,0), 0) 
  
  def test_cals(self):
    cc = calcs(5,10)
    self.assertEqual(cc[0][1], 15)
    self.assertEqual(cc[1][1], -5)
    self.assertEqual(cc[2][1], 50)
    self.assertEqual(cc[3][1], 0)

if __name__ == "__main__":
  unittest.main()
