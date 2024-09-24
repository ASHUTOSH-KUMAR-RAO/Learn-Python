
# ?=>  All About Methods :-

class Heros:

    def __init__(self, name, roll):

        self.name = name
        self.roll = roll

    def Welcome(self):
        print("Kaisa laag raha hai Python se OOps Padh ker 🐻‍❄️")

    def get_roll(self):
        return self.roll


H1 = Heros("IronMan", "Savier")

print("The name of Hero is : ", H1.name)
print("This Hero Roll is as a :-", H1.roll)

H1.Welcome()  # ! Methods ko Call kaar rehe hai hum yeha per

# ? Jaise ki hmko pta hai ki oops mein geter aur seter ke case mein hum methods print naaki call krte hai
print(H1.get_roll())
