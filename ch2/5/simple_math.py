#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# lessons learned:
# - test various assumptions: num2 = 0 needed ZeroDivisionError exception
# - dicts don't have order, so had to use list of tuples to maintain order
# - so overall great that your assumptions are tested by DOING (even this simple exercise)
#
def get_num(n):
  while True:
    num = raw_input("What is the %s number? " % n)
    try:
      num = int(num)
    except:
      print "err: not a number"
      continue
    if num < 0:
      print "err: less than 0"
      continue
    return num

def divide(num1, num2):
  """ watch out for divide by 0 """
  try:
    return num1/num2
  except ZeroDivisionError:
    return 0

def calcs(num1, num2):
  return [
    ("+", num1+num2),
    ("-", num1-num2),
    ("*", num1*num2),
    ("/", divide(num1,num2)),
  ]

if __name__ == "__main__":
  num1 = get_num("first")
  num2 = get_num("second")
  out = []
  results = calcs(num1, num2)
  for op, res in results:
    out.append("%d%s%d = %d\n" % (num1, op, num2, res))
  print "".join(out)
