import os
import re
import math
import sys

def test_top_speed(t,l):
  assert t <= l

def test_pass_fail(res):
  assert res == "PASS!"

def speed_test(mylogfile):
  mykeys = ['timestamp_us','traction_command','traction_speed']
  mydict = {}
  result = "PASS!"
  limit = 0.845000999
  top = 0.0
  with open(mylogfile, 'r') as f:
    for line in f:
      line = line.strip()
      if ':' in line:
        key,value = line.split(':')
        if key in mykeys:
           mydict[key] = value
           if key == 'traction_speed' and top < float(mydict[key]):
             top = float(mydict[key])
           if key == 'traction_speed' and float(mydict[key]) >= limit:
             #print "FAIL!"
             result = "FAIL!"
           elif key == 'traction_command' and float(mydict[key]) > 0.0:
             print(mydict.keys())
             print(mydict.values())
      f.close
    print("top speed:")
    print top
    if top <= limit:
       print result,
       print "<=",
       print limit
    else:
       print result,
       print ">",
       print limit
    assert test_top_speed(top,limit)
    assert test_pass_fail(result)


if __name__ == "__main__":
   if len(sys.argv) <= 1:   # wrong usage
      print "add an argument as log file name"
      print "ex) python myParseColon.py <log file name>"
   else:
      speed_test(sys.argv[1]) 

