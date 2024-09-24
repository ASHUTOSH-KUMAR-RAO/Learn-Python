 
#! WAP to Print a number From N to 1.

def number(n):
  if n == 0:
    return 
  
  # print(n) (N to 1)
  
  ans = number(n-1)
  
  print(n) # (1 to N)
  
  return ans

n = int (input("Enter the value of n is : "))

Result = number(n)

