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

l1 = [1,3,5,7,9]
l2 = [2,4,6,8,11,10,13]
print(merge_sorted_lists(l1,l2))
