
# ? WAP to Sum of n Number is :-

def sum(n):
    if n == 1:
        return 1
    ans = n + sum(n-1)
    return ans


n = int(input("Enter the value of n is :"))

Result = sum(n)

print("The sum of n is ", Result)
