# Average Time complexity O(logN)
# Best case for time complexity: O(1): 
# constant time if the value is in the middle
# Worst case for time complexity: O(n^2): if the value is smallest or largest

def bins(array, val, low, high):
   mid = (low + high) // 2
   if low > high:
     return -1
   if val < array[int(mid)]:
     return bins(array, val, low, mid)
   elif val > array[int(mid)]:
     return bins(array, val, mid+1, high)
   else:
     return mid

if __name__ == "__main__":
   a = [1,2,3,4,5,6,7,8,9,10]
   v = 1
   l = 0
   h = len(a)-1
   print(h)
   m = bins(a,v,l,h)
   print(m, a[m])

