# how many items content in box list?
def check_dic(box, items):
  dic = {}
  for i in items:
    dic[i] = 0
  for i in box:
    if i in dic: 
      dic[i] += 1 
  return dic

box = [1,2,3,4,5,6,7,8,9]
items = [1,5,8,10]
print(check_dic(box,items))
