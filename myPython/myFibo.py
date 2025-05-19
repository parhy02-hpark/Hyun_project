# recursive method
def fibo_recursive(n):
  if n < 2:
    return n
  else:
    return (fibo_recursive(n-1) + fibo_recursive(n-2))

num = 10
for i in range(num):
  print(i, fibo_recursive(i))

# non-recursive method
def fibo_non_re(n):
  c = 0
  first = 0
  second = 1
  while c < n:
    if c <= 1:
      next = c
    else:
      next = first + second
      first = second
      second = next 
    print(c, next)
    c += 1
 
num = 10
fibo_non_re(num)
