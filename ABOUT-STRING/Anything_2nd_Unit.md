# STRINGS :- ✅

## Strings are a sequence of characters enclosed in quotes.
### Strings can be enclosed in single quotes or double quotes.


 ```python
 #How to create a sting:- Multiple Way To Create String

str1 = "Awash Kumar"
str2 = 'Abhisek Kumar Singh'
str3 = """Battery Pandey"""
```
### Escape sequence Character :- used for the formating Purpose, Ex=> tab,nextline etc.

```python
str1 = "Hello\t \World"  # \t for tab
str2 = "Hi Ashutosh aur Question Practise Achi Chal rhi \n hai Babbar ki classes se " # \n for nextline
```
## Adding Two String :- By the help of  Concatination
```python
str1 = "a"
str2 = "b"
str3 = str1 + str2
print(str3)
```
## How to Check String lenght:- By the help of "len".
```python
str1 = "Ashutosh Kumar Rao"
print(len(str1))  # Output:- 17
```
## How to Check String Indexing:- By the help of "Indexing".
```python
==> In terms of string in python indexing always start with 0,ex:- [0,1,2,3,4,5] etc 
str1 = "Ashutosh Kumar Rao"
print(str1[0])  # Output:- A
```

## Slicing In Python:
```python
str1 = "Ashutosh Kumar Rao"
print(str1[0:4])
# Output:- Ashu,not including last elemnt menas 4th(t).
print(str1[0:])  # Output:- Ashutosh Kumar Rao,including all value form 0 to end.
```

# String Functions ==>
```python
1st => endswith() function
str = "I am styding python from self"
print(str.endswith("ege")) # iska mtlb hua ki aab ye check karega ki kya jo maine string likha hai wo ,"ege" ke sath end ho raha hai yedi ho raha hai tp true other wise false de dega
```
```python
2nd => capitalize() == 1st character ko cappitalize karta hai

str = "ashutosh kumar rao"
print(str.capitalize()) # Output:- Ashutosh kumar rao
```
```python
3rd => casefold() == convert string into lower case
str = "ASHUTOSH KUMAR RAO"
print(str.casefold()) # Output:- ashutosh kumar rao
```
```python
4th => replace() == rplace olde occurence to new occurence
str = "Ashutosh Kumar Rao"
print(str.replace("Ashutosh","Rahul")) # Output:- Rahul Kumar Rao
```
```python
5th => split() == split string into list
str = "Ashutosh Kumar Rao"
print(str.split()) # Output:- ['Ashutosh', 'Kumar', 'Rao']
```
```python
6th => join() == join list into string
list1 = ['Ashutosh', 'Kumar', 'Rao']
print(" ".join(list1)) # Output:- Ashutosh Kumar Rao
```
```python
7th => strip() == remove leading and trailing spaces
str = "   Ashutosh Kumar Rao   "
print(str.strip()) # Output:- Ashutosh Kumar Rao
```
```python
8th => lstrip() == remove leading spaces
str = "   Ashutosh Kumar Rao   "
print(str.lstrip()) # Output:- Ashutosh Kumar Rao
```
```python
9th => find() == find the element but print in the form of indexing
str = "Ashutosh Kumar Rao"
print(str.find("o")) # Output:- 6
```
```python
10th => count() ==  find how many times are there in stringbo
str = "Ashutosh Kumar Rao"
print(str.count("o")) # Output:- 2
```

# Setup For Your Local Machine For Running Your Python Program :👋

`python -m venv env` :- Basically it's a setup for Enviornment 

`env\scripts\activate` :- That Means to activate your enviornment for your particular Folder