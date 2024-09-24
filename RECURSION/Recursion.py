
# todo WAP to print FActorial Number using Recursion :-

def factorial(n):
  
  # ? Base Case OR Stoping Condition 🐻‍❄️
  
    if n == 0:
        return 1
      
      # !Recursive Realtion 👍
      
    ans = n * factorial(n-1)
    return ans


n = int(input("Enter the value of n is :"))


# *  Calling the Function ✅

Result = factorial(n)

print("The factorial of a number is: ", Result)
