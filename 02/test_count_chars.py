import unittest
from count_chars import count_chars

class TestHello(unittest.TestCase):

  def test_count_chars(self):
    inp = "bobbelderbos"
    self.assertEqual(count_chars(inp), "%s has %d characters" % (inp, 12))

  def test_empty(self):
    self.assertEqual(count_chars(""), "enter something please")
  

if __name__ == "__main__":
  unittest.main()
