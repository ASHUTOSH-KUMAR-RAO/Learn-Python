
# ? => How to create a Constructor :-

class Car:

    color = "Blue"

    # todo => Constructor mein hamesa ek self argument pass krna padta hai , nhi to syntax error aa jata hai "aur jaruri nhi hai ki hum uska name slef hi iske jagah place per hum kuch bhi de sekte hai , but aurgument slef hi pass krna padta hai".

    def __init__(ashu, modelName, carName):

      #! aur Basically jo data hum pass krte hai aurguments main usko hum attributes bolte hai

        ashu.model = modelName
        ashu.name = carName  # ? => aur aise hi hum constructor ke andar kitna bhi aurgument pass kr sekte hai aur unka acces aise le sekte hai

        # print("Adding New Model")


# *=> aur jo kuch bhi humne Constructor ke aurgument mein pass kiya hai uske element ko hum yeha directly pass kaar sekte hai
C1 = Car(2019, "Scorpio-N")

print(C1.color, C1.model, C1.name)
# print(C1.model)
# print(C1.name)
print("New Car Details below :- ")
C2 = Car(2022, "tata-nano")
print(C2.model, C2.name)
# print(C2.name)
