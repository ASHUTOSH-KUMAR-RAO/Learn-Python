# ABOUT FUNCTIONS :-

- Function is nothing but they are block of code that can be  reusable Code and that can be perform any type of task .

## Types Of Functions :-

1. Buil-in Function. (this Function are laready include in python, Basically it means by default)
2. Useer Defined

### How To Create A function :-

```python
 def Function_Name (Parameter) : # paramter is nothing,but When a  taking input in a function 
    # Code 
    return Expression  # ==>  it Means Function Return , that means we give as a output
```

### How To Call A Function :-

```python
Function_name(arguments)
```

## Types Of Arguments :-

- Positional Arguments.(Means Jaha per Actual Positon hi pass krte hai as an Arguments)
- keyWord Arguments .(iska mtlb hota hai ki yeha per arguments ko as a name pass krte hai .(Named Arguments))
- Default Arguments. , aur ye hamesa as a dictonary ke form me leta hai
- Aurbitary Arguments(variable-legth arguments *args and*kargs). , aur ye hamesa tupel ke from output dega

### Aurbitary Arguments How to Write :-

```python
def addFunction(*args):
    sum = 0
    for i in args
    sum = sum+1
    return sum

    output = addFunction(1,2,3,4)
    print("The sum of number is = ",output)
```

## Pass by Value  :-

- it is a immutable Objects (string,tuple,float,integer)
- when passed a value to a function a copy of the object is created.
- it is assigend in a local variabel in a function.

## Pass by Reference :-

- it is a mutable Objects(List,Dictonary)
- a refrence to actual object passde to a function.
- changeg inside the function will affect the original Objects.
