import math
import pytest
  
def isPrime(n):
  if (n < 2):  
     return False
  elif (n == 2):
     return True
  t = range(n)
  for i in t[2:]:
     if (n % i == 0):
       return False
  return True

def isPrime2(n):
  """Returns True if the number is prime else False."""
  if n == 0 or n == 1:
    return False
  for x in range(2,n):
    if n % x == 0:
       return False
  else:  
    return True

def isPrime3(n):
  for i in range(2,int(n/2)):
     if n%i == 0:
        return False
     else:
        return True
  return True

def test_prime():
  assert isPrime(7)
  assert not isPrime(8)
  assert not isPrime(9)
  assert not isPrime(10)
  assert isPrime(11)
  assert isPrime(23)

def test_prime2():
  assert isPrime2(7)

# simpler implementation...
def test_prime3():
  assert isPrime3(3)
  assert isPrime3(6)
