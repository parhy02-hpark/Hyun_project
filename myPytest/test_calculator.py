import pytest

def add(x,y):
  return x + y

class TestCalculator:
  
  def test_add_positive_numbers(self):
    assert add(2,3) == 5

  def test_add_negative_numbers(self):
    assert add(-2,-3) == -5

