def hello(n=None):
  """ added default arg to ignore raw_input in unittest """
  name = n if n else raw_input('What is your name? ')
  return "Hello, %s, nice to meet you!" % name

def hello_customized(who):
  answers = {
    "tim" : "hi, ",
    "rob" : "bye, ",
    "stef" : "yo, ",
  }
  if not who in answers:
    return False
  return answers[who] + who

if __name__ == "__main__":
  print hello()
  print hello_customized("tim")
