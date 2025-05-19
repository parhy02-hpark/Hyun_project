# anagram is same numbers of letters and same letters in string
def are_anagram(s1, s2):
  print(sorted(s1))
  print(sorted(s2))
  return sorted(s1) == sorted(s2)

str1 = input("enter the string1: ")
str2 = input("enter the string2: ")

if are_anagram(str1, str2) == True:
  print("Anagram!")
else:
  print("Not!")

