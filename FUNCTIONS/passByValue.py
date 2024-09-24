def inner(x):
  # ! Pass By Value
    x = x+1
    print("Inside The function is :", x)


x = 5
print("Outside the function is :", x)
inner(x)

