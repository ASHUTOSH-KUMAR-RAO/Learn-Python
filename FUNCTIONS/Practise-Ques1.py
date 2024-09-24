
#! WAP to calculate a Factorial NUmber

def factorial(n):

    ans = 1

    if n == 0:
        ans = 1
    else:
        for i in range(1, n+1):
            ans *= i
    return ans


n = int(input("Enter the value of n is :"))

output = factorial(n)

print("The factorial of a number is : ", output)
