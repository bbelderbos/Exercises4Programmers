import re
import unittest
from print_quotes import print_quotes

class TestQuotes(unittest.TestCase):

  def test_quote_format(self):
    self.assertIn("Peter Drucker says, \"People are effective because they say 'no,' because they say, 'this isn't for me'.\"", print_quotes())
    self.assertIn("John Maxwell says, \"You cannot overestimate the unimportance of practically everything.\"", print_quotes())

if __name__ == "__main__":
  unittest.main()
