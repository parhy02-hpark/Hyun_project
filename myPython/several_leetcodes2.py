# Find the index of the first occurrence in a String
def strStr(haystack, needle):
    if not needle:
        return 0  # Per problem definition

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1

haystack = "ksadbutsad"
needle = "sad"
print(strStr(haystack, needle))

# search insert position
def searchIns(nums: list, target: int):
    if nums[0] > target:
        return 0
    for i in range(1,len(nums)):
        if nums[i] >= target:
            return i
    if nums[-1] < target:
        return i+1
        
nums = [1,3,5,6]
target = 5
print(searchIns(nums, target))
target = 2
print(searchIns(nums, target))
target = 8
print(searchIns(nums, target))

# length of last word
def lenLastword(s: str):
    words = s.split()
    print(words)
    sum = 0
    for ch in words[-1]:
        sum += 1
    return sum

text = "Hello World"
print(lenLastword(text))
text = "   fly me   to   the moon   "
print(lenLastword(text))
text = "luffy is still joyboy"
print(lenLastword(text))

# plus one
def plusOneList(li: list):
    length = len(li)
    num = 0
    while length > 0:
        num += 10**(length-1) * li[len(li)-length]
        length -= 1
    newnum = num + 1
    return list(map(int, str(newnum)))

digits = [9]
print(plusOneList(digits))
digits = [1,2,3]
print(plusOneList(digits))
digits = [4,3,2,1]
print(plusOneList(digits))

# add binary
def addBin(a: str, b: str) -> str:
    i, j, carry = len(a) - 1, len(b) - 1, 0
    result = []

    # process both strings from right to left
    while i >= 0 or j >= 0 or carry:
        # add corresponding bits and carry
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        
        # append the current bit to the result
        result.append(str(carry % 2))
        carry //= 2

    # return the result as a string
    return ''.join(reversed(result))

a = "1010" 
b = "1011"
print(addBin(a, b))
        
# maximum difference between increasing elements
def maxDiff(nums: list):
    max_diff = -99
    min_value = nums[0]
    for num in nums[1:]:
        if num > min_value:
            max_diff = max(max_diff, num - min_value)
        elif max_diff < 0:
            max_diff = max(max_diff, num - min_value)
        min_value = min(min_value, num)
    print(max_diff)

nums = [1,5,2,10]
maxDiff(nums)
nums = [7,1,5,4]
maxDiff(nums)
nums = [9,4,3,2]
maxDiff(nums)
nums = [9,5,3,0]
maxDiff(nums)

# median of two sorted arrays
import math
def medianTwosorted(list1: list, list2: list):
    i, j = 0, 0
    merged_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    print(merged_list)
    if len(merged_list) % 2 == 1:
        print(merged_list[round(len(merged_list)/2)])
    else:
        mid1 = merged_list[round(len(merged_list)/2-1)]
        mid2 = merged_list[round(len(merged_list)/2)]
        print(mid1)
        print(mid2)
        print((mid1 + mid2) / 2)
    
nums1 = [1,2,6]
nums2 = [3,4,5]
medianTwosorted(nums1, nums2)


def longestSubstring(s: str) -> int:
    char_map = {}
    max_len = 0
    i = 0
    for j, char in enumerate(s):
        if char in char_map and char_map[char] >= i:
            i = char_map[char] + 1

        char_map[char] = j
        max_len = max(max_len, j - i + 1)
    return max_len

print(longestSubstring("abcabcbb"))
print(longestSubstring("pwwkew"))
