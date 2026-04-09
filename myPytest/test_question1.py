import pytest
# question 1 py test code
# py.test -v test_question1.py

import os
from myCalc import myCalc


myObj = Calculator()

def test_add():
  myObj.add(4)
  assert myObj.getValue() == 4

def test_subtract():
  myObj.add(2)
  assert myObj.getValue() == 2

def test_mult():
  myObj.add(3)
  assert myObj.getValue() == 6

def test_divide():
  myObj.add(2)
  assert myObj.getValue() == 3

