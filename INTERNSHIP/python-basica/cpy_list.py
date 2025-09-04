
# list1 = [1,2,3,4,5]

# list2 = list1

# print(list2)

sent1 = "kaise ho kaha jaa rehe h "
ashu = 0

for i in sent1: 
    if i == " ":
        ashu = ashu-1
print(ashu+1)


#! Number Of A Count

str1 = "Ashutosh Kumar Rao KAise ho Kaha Ja REhe Ho"

str2 = str1.count("a")

print("Number of a is :-",str2)

# TOdo=> Functions :- 

def myName():
    print("my Name is Ashutosh Kumar rao")

myName()


def myList():
    liste1 = [1,2,3]
    print(liste1)
myList() 


elist = []
print(type(elist))
lst = [6]
print(lst)

fest1 = ()
print(type(fest1))
# todo => Create a funtion that take list and print its avg:-

def take1Tuple():
    tup1= (1,4,5,6,7)
    print(max(tup1))
take1Tuple()

def takeTuple():
    tup1 = (1, 4, 5, 6, 7)
    sorteTup = sorted(tup1) #? Jaab Hum Python mein sorted methoda use krte hai then ye revrse chalta hai  
    secondLargest = sortedTup[-2]  # -2 
    print(secondLargest)

takeTuple()

 