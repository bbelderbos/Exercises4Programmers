#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
feet_in_meter = 0.09290304

def get_num(q):                                                                     
  while True:
    num = raw_input(q)
    try:
      num = int(num)                                                                
    except: 
      print "err: not a number"                                                     
      continue
    if num < 0:                                                                     
      print "err: less than 0"                                                      
      continue
    return num  

def calc_area(length, width):
  return length * width

def feet_to_meters(feet):
  return feet * feet_in_meter 

if __name__ == "__main__":
  length = get_num('What is theof the room in feet? ')
  width = get_num('What is the width of the room in feet? ')
  print "You entered dimensions of %d feet by %d feet." % (length, width)
  print "The area is" 
  feet = calc_area(length, width)
  print "%d square feet" % feet
  print "%.3f square meters" % feet_to_meters(feet)
