# 1st basic function decorator
def my_decorator(func):
  def wrapper():
    print("Before calling function.")
    input("pause...")
    result = func()
    input("puase again...")
    print("After calling function.")
    return result
  return wrapper

@my_decorator
def say_hello():
  print("Hello! this is the function using decorator...")

say_hello()

# 2nd argumentis in function
def repeat(n):
  def decorator(func):
    def wrapper(*args, **kwargs):
      for _ in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator

@repeat(3)
def greet(name):
  print("Hello", name)

greet("Park")

# 3rd decorator for measuring execution time
import time

def timer(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(func.__name__, " executed in ", end-start,":", " seconds")
    return result
  return wrapper

@timer
def slow_function():
  time.sleep(2)

slow_function()

# 4th Class method decorator example
def log_method_call(method):
  def wrapper(self, *args, **kwargs):
    print(method.__name__)
    return method(self, *args, **kwargs)
  return wrapper

class Greeter:
  @log_method_call
  def greet(self, name):
    print("Hi, ", name, "!")

g = Greeter()
g.greet("Bob")


# 5th built-in decorator example
class Circle:
  def __init__(self, radius):
    self._radius = radius

  @property
  def radius(self):
    return self._radius

  @staticmethod
  def pi():
    return 3.14159

  @classmethod
  def unit_circle(cls):
    return cls(1)

c = Circle.unit_circle()
print(c.radius)
print(Circle.pi())

