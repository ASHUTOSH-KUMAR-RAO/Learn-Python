
# ! Make a Function which Calculates 'a' raised to the power 'b' using recursion.

def power(a, b):
    if b == 0:
        return 1
    ans = a * power(a, b-1)
    return ans


a = int(input("Enter the value of a is :"))
b = int(input("Enter the value of b is :"))

Result = power(a, b)

print("The Power of a raised to b is :", Result)
