# instance method, static method, class method

class Rectangle:
  count = 0
  def __init__(self, width, height):
    self.width = width
    self.height = height
    Rectangle.count += 1

  # instance method
  def calcArea(self):
    area = self.width * self.height
    return area

  # static method: there is no self parameter and decorator @staticmethod
  @staticmethod
  def isSquare(rectWidth, rectHeight):
    return rectWidth == rectHeight

  # class method: there is no self parameter but there is cls parameter
  @classmethod
  def printCount(cls):
    print(cls.count)

  def __add__(self, other):
    obj = Rectangle(self.width + other.width, self.height + other.height)
    return obj

r1 = Rectangle(10,5)
print(f"r1= {r1}")
r2 = Rectangle(20,10)
print(f"r2= {r2}")
r3 = r1 + r2
print(f"r3= {r3}")

# Test
square = Rectangle.isSquare(5,5)
print("square = ", square)

rect1 = Rectangle(5,5)
rect1.printCount()
rect2 = Rectangle(2,5)

