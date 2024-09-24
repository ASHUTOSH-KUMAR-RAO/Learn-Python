
#! Tupels In Python :- 

marks = ("physics","Chemistry")
print(type(marks))
print(marks)


# Methods of tupels:-
# 1. append() :- Add an element to the end of the list
subject = ("Maths","Physics","Ecology")
subject.append("Chemistry")
print(subject)

#2. sort() :- sort in ascending Order & descending order
age = (23,12,15,20)
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