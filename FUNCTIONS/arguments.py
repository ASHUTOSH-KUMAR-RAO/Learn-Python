def add(n1, n2 = 0):
    print("The value of n1 is :", n1)
    print("The value of n2 is :", n2)
    sum = n1+n2
    return sum

# x = 12
# y = 13
                            #?=>   Types Of Arguments :-❤️

# * => print("The sum of x and y is :",add(x,y)) # This is also know as a arguments


#! => print("The sum of x and y is :", add(12, 13))  # Basically this is also know as Positional Arguments

# todo=> print("The sum is :", add(n1=12, n2=13))  This is Called keyword arguments(named arguments).


print("By the help of a Default Arguments :- ",add(12)) #? => Iska mtlb hai ki hum yeha per jiski  value ko pass karenge wahi lega aur jisko value ko hum pass nhi karenge aur jiss value ko pass nhi karte usko zero compulsory hota hai "0" le leta hai 