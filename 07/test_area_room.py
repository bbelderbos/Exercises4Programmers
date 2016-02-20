import unittest
from area_room import *

class TestModule(unittest.TestCase):

  def test_calc_area(self):
    self.assertEqual(calc_area(15, 20), 300)

  def test_feet_to_meters(self):
    self.assertEqual(round(feet_to_meters(300), 3), 27.871)

if __name__ == "__main__":
  unittest.main()
