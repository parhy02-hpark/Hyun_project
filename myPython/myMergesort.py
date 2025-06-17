# merge two sorted lists into one list then sort
def merge_sorted_lists(list1, list2):
  merged_list = []
  i, j = 0, 0

  while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
      merged_list.append(list1[i])
      i += 1
    else:
      merged_list.append(list2[j])
      j += 1
 
  merged_list.extend(list1[i:])
  merged_list.extend(list2[j:])

  return sorted(merged_list)

# remove duplicate numbers in the list
def removeDuplicates(nums):
  if not nums:
    return 0
  
  # pointer for placing unique elements
  k = 1
  for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
      nums[k] = nums[i]
      k += 1
  return k


l1 = [1,2,4]
l2 = [1,3,4]
mergelist = merge_sorted_lists(l1,l2)
print(mergelist)
k = removeDuplicates(mergelist)
print(k)
print(mergelist[:k])
