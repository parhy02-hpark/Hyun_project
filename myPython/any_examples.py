'''
The any() function in Python is a built-in function that takes an iterable as an argument 
and returns True if at least one element in the iterable is truthy. If the iterable is 
empty or all elements are falsy, it returns False. 
'''
# example list of values
values = [0, False, None, []]
#values = [0, False, None, [], "Hello"]

# any() will return True because "Hello" is truthy
result = any(values)
print(result)  # Output: True or False

numbers = [1,3,5,7,8,11]
# check if any number is even
result = any(num % 2 == 0 for num in numbers)
print(result)



