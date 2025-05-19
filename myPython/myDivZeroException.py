# use try, except, else, finally keyword to manipulate the divide by zero case
def divide(x, y):
  print(f"x= {x}")
  print(f"y= {y}")
  try:
    result = x / y
  except ZeroDivisionError:  # this is optional comment.. not necessary
    print("Divided by zero!") 
    return   # important: Exit the function if there is an error
  else:   # this is run when the result does not have the error
    print(f"Result: {result}")
  finally:
    print("This block always executes. Usually close function.")

divide(6,3)
divide(6,0)
divide(4,1)
divide(9,0)
