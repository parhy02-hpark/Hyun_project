def isPalindrome_slicing(s):
  if type(s) != str:
    s = str(s)
  return s == s[::-1]

s = input("Enter the word: ")
if isPalindrome_slicing(s) == True:
  print(s + " is a palindrome")
else:
  print(s + " is not a palindrome.")

def isPalindrome_iterative(s):
  j = len(s)-1
  for i in range(j):
    if s[i] == s[j]:
      flag = True
      j -= 1
    else:
      flag = False
      break
  return flag

s = input("Enter the word again: ")
if (isPalindrome_iterative(s) == True):
  print(s + " is a palindrome by iterative method")
else:
  print(s + " is Not a palindrome by iterative method")
