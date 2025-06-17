# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

def two_Sum(nums: list, target: int):
    num_map = {}
    for i, num in enumerate(nums):
        #print(i, num)
        complement = target - num
        #print(complement)
        if complement in num_map:
            #print("yes")
            return [num_map[complement], i]
        num_map[num] = i

print(two_Sum([2,7,11,15], 26))
print(two_Sum([3,2,4], 6))
print(two_Sum([3,3], 6))
