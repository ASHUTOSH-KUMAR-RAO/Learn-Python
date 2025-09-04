
class Abc:
    def __init__(self):
        print(self)
Ab = Abc()
print(Ab)
print(id(Ab))
print


class Abc:     
    def __init__(self):          # todo=> self is the refrence to current class object
        print(self)


Ab = Abc()
print(Ab)
print(id(Ab))

# Hash codes are already integers in Python
print(hash(Ab))  # Returns integer hash
print(type(hash(Ab)))  # <class 'int'>

# If you have hex string, convert to int:
hex_str = hex(id(Ab))
int_val = int(hex_str, 16)
print(f"Hex: {hex_str}, Int: {int_val}")


# Basic Inheritance Program in Python

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


dog = Dog("Buddy")
cat = Cat("Kitty")


dog.speak() 
cat.speak() 

#? Problem !:-
def sum_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

my_list = [1, 2, 3, 4, 5]
result = sum_list(my_list)
print(f"Sum = {result}")

# ! Problem 2:-
def check_tuple(element, my_tuple):
    if element in my_tuple:
        return True
    else:
        return False

my_tuple = (1, 2, 3, 'hello')
print(f"Is 2 in tuple? {check_tuple(2, my_tuple)}")
print(f"Is 'hi' in tuple? {check_tuple('hi', my_tuple)}")