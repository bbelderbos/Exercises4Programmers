import unittest
from hello import hello, hello_customized

class TestHello(unittest.TestCase):

  def test_hello(self):
    name = "Bob"
    exp = "Hello, %s, nice to meet you!" % name
    self.assertEqual(hello(name), exp)

  def test_hello_diff_msg(self):
    names = ("tim", "rob", "stef")
    greetings = ("hi, ", "bye, ", "yo, ")
    for i,n in enumerate(names):
      gr = greetings[i] + n
      self.assertEqual(hello_customized(n), gr)

  def test_hello_diff_msg_unknown(self):
    self.assertEqual(hello_customized("bob"), False)

if __name__ == "__main__":
  unittest.main()
