# Name: Keaton Caldwell

print("It worked!")

x = 3

example = "im a string" # The variable called example is now holding the string value "im a string"

a = 3 # The variable called [a] is now holding the intiger [3]

b = 4.0 #The variable called [b] is now holding the float [4.0]

c = True #The variable called [c] is now holding the boolean [True]

d = False #The variable called [d] is now holding the boolean [False]

e = "Hey!" #The variable called [e] is now holding the string [Hey!]

f = None #The variable called [f] is now holding the none [none]

age = 32 #The variable called [age] is now holding the intiger [32]

name = "Keaton" #The variable called [name] is now holding the string [Keaton]

instrument = "Guitar" #The variable called [instrument] is now holding the string [Guitar]

'''

a variable Name must start with a letter or the underscore character
a variable cannot start with a number
a variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
Variables names are case sensetive age Age and AGE are different
a variable cannot be any of the python keywords

'''

# name = input("Enter your name:")

# age = input("Type your age:")

# print(name, age, type(name), type(age))

# ask user for two numbers

# first_number = input("whats the first number?")
# secound_number = input("whats the secound number?")

# #convert numbers to intiger versions of themselves

# first_number = int(first_number)

# secound_number = int(secound_number)

# #compares two numbers

# if first_number > secound_number:
#     print(first_number, "Is Bigger")
# elif first_number == secound_number:
#     print("The Numbers Are Equal!")
# else:
#     print(secound_number, "Is Bigger")



name = input("Whats your full name? ")
#calc the length of name
length_of_name = len(name)
#print the length
print(length_of_name)

while " " in name:
    name= name.replace(" ", "")