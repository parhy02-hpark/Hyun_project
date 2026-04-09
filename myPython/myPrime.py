def isPrime(n):
  number = int(n)
  flag = False 
  if number == 0 or number == 1:
    return flag
  elif number == 2:
    flag = True
  elif number > 2:
    for i in range(2,number):
      if number % i == 0:
        flag = False
        break
      else:
        flag = True
  return flag

#num = input("enter the number: ")
if isPrime(9) == True:
  print("Yes, prime!")
else:
  print("No")
