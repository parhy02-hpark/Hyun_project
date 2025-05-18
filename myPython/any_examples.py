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



