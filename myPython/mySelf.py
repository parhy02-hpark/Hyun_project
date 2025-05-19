'''
__init__: assign values & object properties
- is called automatically every time the class is being used to create a new object
self: a reference to the current instance of the class, and is used to access variables
that belong to the class 
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def printname(self):
    print(self.name)

p1 = Person("Ken", 40)
p1.printname()
#print(p1.name, p1.age)

