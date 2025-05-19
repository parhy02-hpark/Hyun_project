import re
import sys

file = open(sys.argv[1], "r")

for line in file:
  if re.search(sys.argv[2], line):
    print(line)
file.close()
