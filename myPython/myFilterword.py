'''
You will be filtering words based on the letters on the letters that they contain.
Specifically, you'll be given an input list of words (all lowercase), along with a set
of lowercase, and asked to keep only the words that contain at least one letter in the 
given set.
'''
def filter_words(words, letters):
  """Filter words to keep only those containing at least one letter from the given set."""
  letters_set = set(letters)
  filtered_words = [word for word in words if any(char in letters for char in word)]
  return filtered_words

#ex)
words = ["apple", "banana", "lemon", "cherry", "grape", "tomato", "orange"]
letters = "le"

print(filter_words(words, letters))
