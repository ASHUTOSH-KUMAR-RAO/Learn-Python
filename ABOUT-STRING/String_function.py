
#! endswith() Functions ==>

str = "I am styding python from self"
print(str.endswith("ege")) # iska mtlb hua ki aab ye check karega ki kya jo maine string likha hai wo ,"ege" ke sath end ho raha hai yedi ho raha hai tp true other wise false de dega

#? capitalize() Functions ==>

str = "hi my self ashutosh kumar rao"
print(str.capitalize()) # iska mtlb hua ki ye 1st character ko capital mein kr deta hai

#* casefold() Function ==>

str = "ASHUTOSH,ABHISEKH,AWASH,JYOTI,BATTERY"
print(str.casefold()) 

#TODO = replace() Function =>

str = "nikita,bhatnagar,rohit,bhram,shahAlam"
print(str.replace("nikita,bhatnagar,rohit,bhram,shahAlam","upendra,apoorva,silpi,bhupesh,pooja"))

#! = find() Function =>
str = "ASHUTOSH,ABHISEKH,AWASH,JYOTI,BATTERY"
print(str.find("ABHISEKH")) # find and also with the indexing no output => 9

#* strip() Function =>
str = "   Ashutosh Kumar Rao   "
print(str.strip()) # Output:- Ashutosh Kumar Rao

#TODO count() Function =>

str = "ASHUTOSH,ABHISEKH,AWASH,JYOTI,BATTERY"
print(str.count("ASHUTOSH")) # Output:- 1

