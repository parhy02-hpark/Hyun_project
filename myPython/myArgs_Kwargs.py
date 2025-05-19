# *args: Arbitrary Positional Arguments
# **kwargs: Arbitrary Keyword Arguments

# purpose: allows a function to accept a variable number of position arguments
def my_function(*args):
  for arg in args:
    print(arg)

my_function(1, "NG", "DoD")
my_function(2, "ASML", "Semiconductor")
my_function(3, "Apple", "Phone")

# purpose: allows a function to accept a variable number of keyword arguments
# such as key:value
def my_function2(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

my_function2(name="Alice", age=38, city="San Diego")
my_function2(name="John", age=40, city="LA", car="MB")
