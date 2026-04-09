def minimizeMax(nums, p):
    nums.sort()

    def can_form_pairs(max_diff):
        count = 0
        i = 1
        while i < len(nums):
            if nums[i] - nums[i-1] <= max_diff:
                count += 1
                i += 2
            else:
                i += 1
        return count >= p
    
    left, right = 0, nums[-1] - nums[0]
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_form_pairs(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer



print(minimizeMax([1,3,6,19,20], 2))
print(minimizeMax([10,1,2,7,1,3], 2))
print(minimizeMax([4,2,1,2], 1))
