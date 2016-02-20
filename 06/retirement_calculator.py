#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from datetime import date

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


if __name__ == "__main__":
  year = date.today().year
  age = get_num('What is your current age? ')
  retire = get_num('At what age would you like to retire? ')
  timeleft = retire - age
  if timeleft < 0:
    print "You can already retire :)"
  elif timeleft == 0:
    print "You can retire this year :)"
  else:
    print "You have %d years left until you can retire." % timeleft
    print "It's %d, so you can retire in %d" % (year, year+timeleft)
