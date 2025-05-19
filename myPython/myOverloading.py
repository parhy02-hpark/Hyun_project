# purpose: To provide a way to call the same method with different kinds or numbers of arguments
# Method Signature: must have the same method name but can be different signatures

class Calculator:
  def add(self, a, b=None, c=None):
    if b is not None and c is not None:
      return a + b + c
    elif b is not None:
      return a + b
    else:
      return a

calc = Calculator()
# add method uses the different number of parameters: this is a polymorphism
print(calc.add(5))
print(calc.add(5,6))
print(calc.add(5,6,7))
