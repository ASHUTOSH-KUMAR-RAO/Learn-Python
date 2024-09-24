
# todo => Pass By Reference:-

def modify(lst):
    lst.append(4)
    print("Inside the value is:", lst)


lst = [1, 2, 3]
modify(lst)
print("outer part is :", lst)
