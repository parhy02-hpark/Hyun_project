# overriding - multiple inheritance and same function name
# purpose: To change or specialize the behavior of an inherited method in the subclass to suit
#          its specific needs.
# Method signature: must have the same name and the same parameter list

class Animal:
  def speak(self):
    print("Generic animal sound")

class Dog(Animal):
  def speak(self):	# overriding the speak() method
    print("Woof!")

class Pig(Animal):	# overriding the speak() method
  def speak(self):
    print("Oink!")

animal = Animal()
dog = Dog()
pig = Pig()

animal.speak()
dog.speak()
pig.speak()

