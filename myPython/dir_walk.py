import os, sys, re
from fnmatch import fnmatch

root = '.'
pattern = "*.py"
count = 0
myList = []
for path, subdirs, files in os.walk(root):
  for name in files:
    #print(name)
    if fnmatch(name, pattern):
      #print(os.path.join(path, name))
      #print(name)
      myList.append(name)

print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)

