# OOps :-

- To map with real world scanario ,we started using object in a code is called object oriented programming.

**Note** :- Basically isese pehle hum jo bhi code likhte the usko hum ya to procedural form mein ya fucntion ke form mein likhte the 

```python

a = 12
b = 13
sum = a+b
print(type(sum))

# basically this is called is Procedural code form 

# jaise ki humko pta hai code ka scanerio aise chalta hai "procedural form -> functional form -> object oriented form"


```

**Deep-Knowledege** :- Bahut logo ki ye nhi pta hoga ki function hum kyu use krte hai iska actual meaning.

- Basically hum function hum isiliye use krte hai ki isese code ki "REDUDANCY Decrease hoti hai" aur Similarly "REUSEABILITY Increase hoti hai " Actual meaning ye hoti hai . 


## Class :-

- Basically it is Nothing But bluePrint for creating object 

```python

# Example => How to create a class in terms of Python

class Student :
  name = "Ashutosh-Kumar-Rao "

# Example => How to create a Object , Basically Object is nothing but instances of class 

s1 = Student()
print(s1.name)

```
## Constructor :- 

- Basically Constructor is also known as "_ _init_ _ Function" ,which is always Executed when the Object is being initiated 

- Aur Basically Constructor Function Object creation ke time per Invoked(Execute) hota hai.

- Constructor Basically Object ke Initialisation ke liye hota hai 

```python

Example :-


# ? => How to create a Constructor :-

class Car:
  
  color = "Blue"
  
  def __init__(ashu,modelName,carName):  #  Constructor mein hamesa ek self argument pass krna padta hai , nhi to syntax error aa jata hai "aur jaruri nhi hai ki hum uska name slef hi iske jagah place per hum kuch bhi de sekte hai".
    
    ashu.model = modelName
    ashu.name = carName # aur aise hi hum constructor ke andar kitna bhi aurgument pass kr sekte hai aur unka acces aise le sekte hai 
    
    print("Adding New Model")
    
C1 = Car(2019,"Scorpio-N") # aur jo kuch bhi humne Constructor ke aurgument mein pass kiya hai uske element ko hum yeha directly pass kaar sekte hai

print(C1.color)
print(C1.model)
print(C1.name)

```

**Note 1** :- Aur jaise ki pta hai python by default pehle se Constructor bna leta hai

**Note 2** :- The self parameter is a reference to the current instance of the class, and is used to access of variable that belongs to the class.

**Note 3** :- class Attributes se jyada Object Attributes ki precedense hoti hai 

          class Attr < object Attr

**Note 4** :- We know That class is nothing but it is a collection of Data(Attributes) and Methods .

## Methods :-

- Methods are nothing its a function that belongs to object ,Ex:- String,Dictonary,List.

```python

# How to Use Methods InSide The obj


# ?=>  All About Methods :-

class Heros:

    def __init__(self, name, roll):

        self.name = name
        self.roll = roll

    def Welcome(self):  # Nothing but This is called Methods, aur dekha jaye class ke andar jo function hota ha unko hi hum as a Methods Bolte hai 
        print("Kaisa laag raha hai Python se OOps Padh ker 🐻‍❄️")

    def get_roll(self):
        return self.roll


H1 = Heros("IronMan", "Savier")

print("The name of Hero is : ", H1.name)
print("This Hero Roll is as a :-", H1.roll)

H1.Welcome()  # ! Methods ko Call kaar rehe hai hum yeha per

# ? Jaise ki hmko pta hai ki oops mein geter aur seter ke case mein hum methods print naaki call krte hai
print(H1.get_roll())


```

##   Static Methods :-

- A Methods that don't use the self Parameter(work at the class level)

**Note 1** :- yeha per Work at the class level ka mtlb ye hai ki ye class level per kaam krta hai isiliye ye self parameter nhi leta hai , kyuki hum hamesa self parameter object ke liye lete hai.

```python

Example :-

class Fecaulty:

    name = "Ashutosh Kumar - Rao"

    @staticmethod  # it is also knwon as decorator
    def College():
        print("This is Static Method mean no use any type of self parameter")


S1 = Fecaulty

print(S1.name)

S1.College()

```


# Pillars Of OOps is :-

- Abstraction
- Encapsilation
- Polymorphisum
- Inheritance



[IMPORTANT BOOK PDF](https://wesmckinney.com/book/python-basics)