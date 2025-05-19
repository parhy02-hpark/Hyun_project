'''
Iterators and generators are tools for working with sequences of data in Python, focusing on
memory efficiency and on-demand computation.

An iterator is an object that enables traversal through a sequence of data. It implements the
iterator protocol, which consists of two methods:
__iter__(): Returns the iterator object itself.
__next__(): Returns the next item from the sequence. If there are no more items, 
it raises a StopIteration exception.
'''
my_list = [1,2,3]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))

'''
A generator is a function that uses the yield keyword to return a sequence of values.
When a generator function is called, it returns a generator object, which is an iterator.
Each time yield is encountered, the generator function pauses and returns the yielded value.
When the next value is requested, the function resumes from where it left off.
'''
def my_generator(n):
  i = 0
  while i < n:
    yield i
    i += 1

gen = my_generator(3)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
