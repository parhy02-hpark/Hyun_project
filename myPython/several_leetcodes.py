# this is to test palindrome with slicing... 
def isPalindromeNum(n: int):
    if type(n) == int:
        n = str(n)
    return n == n[::-1]

def isPalindromeNum2(n: int):
    if type(n) == int:
        n = str(n)
    reversed_str = ""
    for ch in n:
        reversed_str = ch + reversed_str
    return n == reversed_str
    
num = input("enter palindrome number: ")
if int(num) >= 0:
    if isPalindromeNum2(int(num)):
        print("true")
    else:
        print("false")
else:
    print("false")


# roman to integer 
# I => 1, V => 5, X => 10, L => 50, C => 100, D => 500, M => 1000
# ex) 2 is written as II, 27 is written as XXVII 
# I can be placed before V (5) and X(10) to make 4 and 9
def roman2Int(s: str):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)-1):
        if roman_map[s[i]] < roman_map[s[i+1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]
    total += roman_map[s[-1]]
    return total

romanStr = input("enter Roman numerals, such as IV: ")
if len(romanStr) > 15:
    print("violating contraints: more than 15 characters..")
else:
    print(roman2Int(romanStr))

'''
Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

# longest common prefix
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Start with the prefix as the first string
    prefix = strs[0]

    # Compare the prefix with each string in the array
    for string in strs[1:]:
        # Reduce the prefix until it matches the start of the string
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
        
    return prefix

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
strs = ["dog", "docecar", "car"]
print(longestCommonPrefix(strs))

# valid parentheses
def validParentheses(s: str) -> bool:
    stack = []
    bracket_map = {
        ')': '(',
        '}': '{', 
        ']': '['
    }

    for ch in s:
        if ch in bracket_map.keys():  # if the character is a closing bracket
            # Get the top element from the stack. If stack is empty, assign a dummy value.
            top_element = stack.pop() if stack else '#'

            # check if the popped element is the correct opening bracket
            # if not, or if stack was empty (top_element was '#'), it's an invalid string
            if bracket_map[ch] != top_element:
                return False
        else:   # if the character is an opening bracket
            stack.append(ch)        
     
     # After iterating through the entire string, if the stack is empty,
     # all brackets were matched correctly.
    return not stack

print(validParentheses("[]{}()"))
print(validParentheses("[{]}"))
print(validParentheses("[[{()}]]"))

# remove elements
def removeElement(val: int, list_l: list):
    k = 0
    for i in range(len(list_l)):
        if list_l[i] != val:
            list_l[k] = list_l[i]
            k += 1

    return k, list_l[:k]

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(val, nums))

# integer to roman
def int2roman(num):
    val = [1000, 900, 500, 400, 
           100, 90, 50, 40,
           10, 9, 5, 4,
           1]
    syb = ["M", "CM", "D", "CD",
           "C", "XC", "L", "XL",
           "X", "IX", "V", "IV",
           "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

print(int2roman(499))

