myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
name = input("What is your name? Maria")
print(name)
color = input("What is your favorite color? Blue ")
animal = input("What is your favorite animal? Dog ")
print("{aria}, you like a {Blue}{Dog}!".format(name,color,animal))