import unittest
from 5-simple_math import divide, calcs

class TestModule(unittest.TestCase):

  def test_divide(self):
    self.assertEqual(divide(4,2), 2)

  def test_f2(self):
    pass

if __name__ == "__main__":
  unittest.main()
