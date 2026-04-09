# Calcualtor class 

class Calculator(object):
  def __init__(self):
    self.value = 0
  def add(self, val):
    self.value += val
  def subtract(self, val):
    self.value -= val
  def mult(self, val):
    self.value *= val
  def divide(self, val):
    self.value /= val
  def getValue(self):
    return self.value

cal = Calculator()
print(cal.value)

