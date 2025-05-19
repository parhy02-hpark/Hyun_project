'''
The zip() function in Python creates an iterator that aggregates elements from multiple 
iterables (like lists, tuples, or strings). It returns an iterator of tuples, where 
the i-th tuple contains the i-th element from each of the input iterables. 
The iterator stops when the shortest input iterable is exhausted. 
'''
# two lists
names = ["Alic", "Bob", "Charlie"]
ages = [30, 25, 45]

# zip() iterator
zipped = zip(names, ages)
print(list(zipped))

for name, age in zip(names, ages):
   print(name, " is ",  age,  " years old.")

# three lists
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 45]
cities = ["New York", "Seoul", "San Diego"]

# zip() iterator
zipped = zip(names, ages, cities)
print(list(zipped))

# different length iterables
li1 = [1,2,3,4,5]
li2 = ['a','b','c']

print(list(zip(li1,li2)))

# string
st1 = "abc"
st2 = "xyz"
# zip() iterator
zipped = zip(st1, st2)
print(list(zipped))

# tuple
tup1 = (10,20,30)
tup2 = ('p','q','r')
# zip() iterator
zipped = zip(tup1, tup2)
print(list(zipped))

# combining different iterable types
my_list = [1,2,3]
my_tuple = ('a','b','c')
my_string = "xyz"
# zip() iterator
zipped = zip(my_list, my_tuple, my_string)
print(list(zipped))

