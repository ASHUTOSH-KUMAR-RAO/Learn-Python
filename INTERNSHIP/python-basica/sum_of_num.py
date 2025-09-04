# Assignment Day02 - Complete Solutions
# Sabhi questions ke solutions with Hinglish explanations

print("="*60)
print("ASSIGNMENT DAY02 - ALL SOLUTIONS")
print("="*60)

# Question 3: Even numbers check
print("\n3. **Even numbers check**")
def is_even(num):
    """
    Ye function check karta hai ki number even hai ya odd
    Even number wo hota hai jo 2 se divide ho jaye without remainder
    """
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

# Test karte hain 1 se 20 tak
print("Numbers 1 to 20 ka even/odd check:")
for i in range(1, 21):
    print(is_even(i))

print("\n" + "-"*50)

# Question 4: Multiplication table
print("\n4. **Multiplication table**")
def multiplication_table(n):
    """
    Ye function kisi bhi number ka table print karta hai
    1 se 10 tak multiply karta hai
    """
    print(f"Multiplication table of {n}:")
    for i in range(1, 11):
        result = n * i
        print(f"{n} x {i} = {result}")

# Example: 7 ka table
multiplication_table(7)

print("\n" + "-"*50)

# Question 5: Factorial of a number
print("\n5. **Factorial of a number**")
def factorial(n):
    """
    Factorial matlab n! = n × (n-1) × (n-2) × ... × 1
    Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
    """
    if n < 0:
        return "Factorial negative numbers ka nahi hota"
    elif n == 0 or n == 1:
        return 1
    
    fact = 1
    print(f"Calculating factorial of {n}:")
    for i in range(1, n + 1):
        fact = fact * i
        print(f"Step {i}: {fact}")
    
    return fact

# Test factorial
result = factorial(5)
print(f"5! = {result}")

print("\n" + "-"*50)

# Question 6: Sum of even numbers
print("\n6. **Sum of even numbers**")
def sum_even_numbers():
    """
    1 se 50 tak ke sabhi even numbers ka sum nikalna hai
    Even numbers: 2, 4, 6, 8, 10, ..., 50
    """
    total = 0
    even_numbers = []
    
    for i in range(1, 51):
        if i % 2 == 0:  # Agar number even hai
            total += i
            even_numbers.append(i)
    
    print("Even numbers between 1 and 50:")
    print(even_numbers)
    print(f"Sum of all even numbers: {total}")
    return total

sum_even_numbers()

print("\n" + "-"*50)

# Question 7: Prime number check
print("\n7. **Prime number check**")
def is_prime(num):
    """
    Prime number wo hota hai jo sirf 1 aur khud se divide hota hai
    Example: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29...
    """
    if num < 2:
        return False
    
    # 2 se lekar sqrt(num) tak check karte hain
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test prime numbers from 1 to 30
print("Prime numbers from 1 to 30:")
prime_numbers = []
for i in range(1, 31):
    if is_prime(i):
        prime_numbers.append(i)
        print(f"{i} is prime")

print(f"All prime numbers: {prime_numbers}")

print("\n" + "-"*50)

# Question 8: Reverse order printing
print("\n8. **Reverse order printing**")
def reverse_printing():
    """
    Numbers ko 20 se 1 tak print karna hai reverse order mein
    range(start, stop, step) use karते hain
    """
    print("Numbers from 20 down to 1:")
    for i in range(20, 0, -1):  # 20 se start, 0 tak (exclusive), -1 step
        print(i, end=" ")
    print()  # New line ke liye

reverse_printing()

print("\n" + "-"*50)

# Question 9: Grades using if-else
print("\n9. **Grades using if-else**")
def grade(marks):
    """
    Marks ke basis par grade assign karna hai:
    90+ = A, 75+ = B, 50+ = C, otherwise = Fail
    """
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

# Different marks test karte hain
test_marks = [95, 85, 65, 45, 30]
print("Grade calculation for different marks:")
for mark in test_marks:
    result = grade(mark)
    print(f"Marks: {mark} → Grade: {result}")

print("\n" + "-"*50)

# Question 10: Fibonacci sequence
print("\n10. **Fibonacci sequence**")
def fibonacci(n):
    """
    Fibonacci sequence: har number pichle 2 numbers ka sum hota hai
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
    Formula: F(n) = F(n-1) + F(n-2)
    """
    if n <= 0:
        print("Please enter positive number")
        return
    
    print(f"First {n} terms of Fibonacci sequence:")
    
    # Pehle 2 terms
    a, b = 0, 1
    
    if n == 1:
        print(a)
        return
    
    print(a, b, end=" ")

    # Baaki terms calculate karte hain
    for i in range(2, n):
        c = a + b  # Next term = sum of previous 2 terms
        print(c, end=" ")
        a, b = b, c  # Update for next iteration
    
    print()  # New line

# 10 terms print karte hain
fibonacci(10)

print("\n" + "="*60)
print("ALL SOLUTIONS COMPLETED!")
print("="*60)j