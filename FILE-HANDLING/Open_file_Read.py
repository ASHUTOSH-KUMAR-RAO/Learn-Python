
# todo                                    READ  MODE  ✅

f = open("C:\\Users\\aashu\\Desktop\\Chai aur Tapri\\Unit = 5\\ABOUT.md", "r")
# ? Basically hum ye isiliye 10 likhe jisese hmko shirf starting ke 10 hi words read krne hai
data = f.read(10)
print(data)
print(type(data))

f.close()
