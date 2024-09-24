
# todo WAP to Print Fibbonacci Sequence :-

def fibbonaci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    ans = fibbonaci(n-1) + fibbonaci(n-2)
    return ans


n = int(input("Enter the value of n is :"))

for i in range(1, n+1):

 result = (fibbonaci(i))

 print("The Fibbonacci Sequence is : ", result)
