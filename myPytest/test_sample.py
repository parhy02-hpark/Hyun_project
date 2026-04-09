import pytest
# sample pytest code

def inc(x):
  return x + 1

def mult(x,y):
  return x*y

def test_answer():
  assert inc(3) == 4

def test_answer2():
  assert inc(4) == 5

'''
cmdopt = 'type1'
def test_answer3(cmdopt):
  if cmdopt == "type1":
    print("first")
  elif cmdopt == "type2":
    print("second")
  assert 1
'''

def test_answer4():
  assert mult(3,4) == 12

def test_answer5():
    assert mult(33,445) == 14685
