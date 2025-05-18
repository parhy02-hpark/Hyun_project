# string manipulation: reverse a string

def reverse_string(s):
  return s[::-1]

mystring = "testtest"
print(reverse_string(mystring))

# algorithm of reverse string
def reverse_string(s):
  reversed_s = ""
  for ch in s:
    reversed_s = ch + reversed_s
  return reversed_s

s = input("Enter string: ")
print(reverse_string(s))

