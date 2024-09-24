# <== = = = = = = = = = = = = = Expression Execution  = = = = = = = = = = = =>

# ! ==> When String &  Numeric values can operate together with * == Then Its Repeating
#                    ⬇️

a,b = 2,3
Txt = "@" # Type Of String
print( 2 * Txt * 3) # Output: @@@@@@


# TODO ==> When String & String can Operate with + == Then Its Concatination (string + string)
  #                                ⬇️

a,b = "2",3
Txt = "@"
print((a+Txt) * b) #2@2@2@


# ? ==> When values can operate with all arithmetic operations

#                                ⬇️

c,d = 2,3
e = 5
print((c+d)*e) # 17

# ! ==> When Arithmetic expression with Integer and Float will result == float

#                                ⬇️

A,B = 12,3.0
c =  A * B
print(c) # 36.0

# ? ==> When Result of division operator with two integers will be float

#                                ⬇️
A,B = 12,3
c =  A / B
print(c) # 4.0

# TODO ==> When Integer division with float and int will give int displayed as a flota (but value ata hai int mein hi lekin internally usko typecasting ki wajah se float mein displayed karta hai)

#                                ⬇️

A,B = 12,3.0
c =  A // B
print(c) # 4.0


