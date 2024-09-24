marks = [8.77,8.95,8.88,8.45,5.27]
print(type(marks))
print(len(marks))
print(marks[2])
print(marks)

# List Is a mutable , but String is a emutabel
markss = [7.55,8.75,8.92,10.11]
markss[2] = 9.00
print(markss[1:3])
print(markss)


# Methods of List :-

# 1. append() :- Add an element to the end of the list
subject = ["Maths","Physics","Ecology"]
subject.append("Chemistry")
print(subject)

#2. sort() :- sort in ascending Order & descending order
age = [23,12,15,20]
print(age.sort())
age.sort(reverse=True) # for descending order
print(age.append(32))
print(age)

#3 reverse() :- That menas reverse The Value 
age.reverse()
print(age)

#4 pop() :- Remove the element at index
age.pop(2)
print(age)

#5 remove() :- Remove the value , in case element are more then 1 times then the 1st element remove.
age.remove(20)
print(age)

copyValue = age.copy()
print(copyValue)