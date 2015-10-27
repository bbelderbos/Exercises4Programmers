def count_chars(inp=None):
  if inp == None: # inp None param to test without raw_input
    inp = raw_input('What is the input string? ') 
  if inp == "":
    return "enter something please"
  return "%s has %d characters" % (inp, len(inp))

if __name__ == "__main__":
  print count_chars()
  print count_chars("bob")
