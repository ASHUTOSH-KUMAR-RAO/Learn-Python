x = 12
y = 13

if x < y:
    pass


i = 1
while i < 6:
    print(i)
    i = i + 1

i = 1

print(" ")

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print(" ")

i = 1
while i < 6:
    i = i+1
    if i == 3:
        continue
        print(i)

print(" ")

friends1 = ["Awash", "Abhishek"]
friends2 = ["Battery", "Jyoti"]

for x in friends1:
    for y in friends2:
        print(x, y)


print(" ")
x = lambda a:a+10

print(x(10))


# ! A lambda function is a small anonymous function.

# todo A lambda function can take any number of arguments, but can only have one expression.


txt = "The best things in life are free!"
print("free" in txt)

print(" ")  

x = "Ashutosh" # Slice ke case mein starting ke nhi leta but end ka leta hai 
# aur yehi range ke case mein starting ka leta hai end ka nhi leta hai 

print(x[3:6])