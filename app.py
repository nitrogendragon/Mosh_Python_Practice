import math
import converters
from utils import find_max
from converters import kg_to_lbs
# verbose
# import ecommerce.shipping
#
# ecommerce.shipping.calc_shipping()
# # get specific function
# from ecommerce.shipping import calc_shipping
#
# calc_shipping()
# # get the module
# from ecommerce import shipping
#
# shipping.calc_shipping()
# print('Corey Duncan')
# print('o----')
# print(' ||||')
# print('*' * 10)#mutliple calls to print the asterisk
# price = 10
# price = 20
# rating = 4.9
# print (rating)
# price = float(price)
# print('price' + str(price))
# is_published = False
# if ( is_published == False):
#     rating *= price
#     print(rating)
#
# Name = 'John_Smith'
# age = 20
# new_patient = True

# ask user name and print greeting name

# #get input
# name = input('please enter your name ')
# #print Hi + input
# print('Hi ' + name)

# #Ask the person's name and favourite color. Then print a message saying "person likes color"
#
# #ask for the name and store in a variable name
# name = input("What is your name?")
# #ask for the favourite color and store it in a variable color
# color = input("What is your favourite color?")
# #print the name likes color
# print(name + ' likes ' + color)

# birth_year = input('Birth Year: ')
# #get the type of birth_year
# print(type(birth_year))
# #get the type of age
# print(type(age))
# age = 2019 - int(birth_year)
# print(age)

# Ask a user their weight(in pounds), convert it to kilograms and print on the terminal
# set up kilograms conversion variable
# kilograms = 2.2
# #get weight
# pounds = input("what is your weight in pounds?")
# #convert to kilograms and store in weightK variable
#
# weightK = float(pounds) / kilograms
# #print the weight in kilograms
# print('You weigh '+str(weightK)+' kilograms')

# handling quotes in comment
# course = "Python's Course for Beginners"
# print(course)
# #handling double quotes in string
# course = 'Python"s Course for Beginners'
# print(course)
# multiLine string
# course = '''
# Hi John,
#
# Here is our first email to you
#
# Thank you,
# The support team
#
# '''
# # print(course)

# course = 'Python for Beginners'
# #getstring character at index
# print(course[0])
# #reverse order selection index
# print(course[-1])
# #extract several characters starting at index a and going up to index b
# print(course[0:3])
# #return string in reverse order
# print(course[::-1])
# #return selection in reverse starting at index A and going back to index B(not including index B
# print(course[4:1:-1])

# #copy value of course into another
# another = course[:]
# # #print to show
# # print(another)

# set up name
# name = 'Jennifer'
# #test what happens when you set the end value to -1
# print(name[1:-1])#we get the second character up to the second to last character including the second to last character that is

# first = 'John'
# last = 'Smith'
# #inneficient way to concatenate into a message
# message = first + ' [' + last + '] is a coder'
# print(message)
# #formatted strings example *****
# #start with fthen quotes and normal text is applied normally as you would want it
# #curly brackets let you dynamically put in varaible values
# msg = f'{first} [{last}] is a coder'
# print(msg)

# # python string capabilities
# course = 'Python for Beginners'
# # get the length of the string
# print(len(course))
# # len is a general purpose string
# # upper and lower case functions
# # use a . (dot) function.. called a method
# print(course.upper())
# print(course.lower())
# # does not modify original if we just print
# print(course)
# # find method to find character and its index
# # find is case sensitive and returns the first occurrence
# print(course.find('P'))  # 0 is the result
# # replace characters
# print(course.replace('Beginners', 'Absolute Beginners'))
# # checking for existence of using 'in' operator returns true or false at a base level
# # note it is also case sensitive
# print('Python' in course)

# #arithmetic operators
# print(10+1)
# # float division
# print(10/3)
# #int division
# print(10//3)
# # modulus aka remainder
# print(10%3)
# # exponents
# print(10 ** 2)
# # augmented assignment operator
# x=10
# # adds 3 to x for 13
# x=x+3
# #augmented version
# x +=3
# # print it and...
# print(x)
# #augmented subtraction
# x-=3
# print(x)
# # order of operations (PEMDAS) but its more advanced in programming but not too important to know atm
# x = (10+3) *2 ** 2
# print(x)

# # Math Functions
# x=2.9
# print(round(x))
# print(abs(-2.9))
#
# #Modules: organize our code into different sections
# #Math Module: import math
# print(math.ceil(2.9))
# print(math.floor(2.9))
# # browser search: python 3 math module : leads to documentation of math module...

# #if statements
# is_hot = False
# is_cold = False
# if is_hot:
#     #using  '\n' tells python to jump a line
#     print("It's a hot day\n")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

# # bank downpayment problem
# '''
# Price of house is $1m
# if buyer has good credit,
#     they need to put down 10%
# otherwise
#     they need to put down 20%
# print the payment
# '''
# cost = 1000000
# downpayment = 0
# good_credit = False
# if good_credit:
#     downpayment = cost * .1
# else:
#     downpayment = cost * .2
# print(f"Down payment: ${downpayment}")

# #Logical Operators
# #if applicant has high income AND good credit they are eligible for loan
# has_high_income = True
# has_good_credit = False
# _has_criminal_record = True
# #and logic statement
# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# #Or logic
# if has_good_credit or has_high_income:
#     print("Eligible for loan")
# #not logic
# if has_good_credit and not _has_criminal_record:
#     print("eligible for loan")
# else:
#     print("Not Eligible")

# # Comparison Operators
# '''
# > greater than
# < less than
# == equal to
# >= greater than or equal to
# <= less than or equal to
# '''
# temperature = 30
# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")
# Problem: If name is less than 3 characters
# print name must be at least 3 characters
# otherwise if it's more than 50 characters long
# print name can be a maximum of 50 characters
# otherwise
# print name looks good

# name = ''
# # while loop to keep it going until the desired input
# while len(name)<3 or len(name)>10:
#     name = input("Please enter a name")
#     if len(name) <3:
#         print("name must be at least 3 characters long")
#     elif len(name)>10:
#         print("name cannot be greater than 10 characters")
#     else:
#         print(f'''Username {name} is available
#     welcome to loner simulator 12''')

# #Project: weight converter
# weight = input("enter your weight: ")
# weight_type = ''
# while weight_type != 'l' and weight_type != 'L' and weight_type != 'k' and weight_type != 'K':
#     weight_type = input("Is this in (L) pounds or (K) kilograms? ")
#         print(f" you weigh {float(weight) /2.2} kilograms")
#     else:
#         print(f"You weigh {weight}lbs")
#     print(weight_type)

# # while loops
# #while condition: repeats code in block
# #   block...
# i=1
# while i <=5:
#     #multiplying times that the asterisks is displayed
#     print('*' * i)
#     i = i + 1
#     print("Done")

# # Guessing Game
# number = 5
# guess = 0
# tries = 0
# while guess != number and tries != 3:
#     tries += 1
#     guess = int(input('guess a number: '))
#     if guess == number:
#         print("You win!")
#         # you can exit or break the loop with a break statement
#         break
#     elif tries == 3:
#         print("Sorry, you lose")
#     else:
#         print(f"You have {3 - tries} chances remaining")

# #Car game
# started = False
# while True:
#     #DRY- don't repeat yourself
#     command = input(">").lower()
#     if command.lower() == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to exit
#         """)
#     elif command == "start" and not started:
#         started = True
#
#         print("Car started... Ready to go!")
#     elif command == "start":
#         print("Your car is already running")
#     elif command == "stop" and started:
#         started = False
#         print("Car stopped.")
#     elif command == "stop" and not started:
#         print("You already stopped")
#     elif command == "quit":
#         exit()
#     else:
#         print("I don't understand that...")


# # For Loops: iterate over items of a collection
# # in: checks all items like characters in a string
# #check all the items in the string Python
# for item in 'Python':
#     print(item)
# #lists
# for item in ['Mosh', 'John', 'Sarah']:
#     print(item)

# # Range to go through a certain range of numbers
# #get items in a range of 10 items
# for item in range(10):
#     print(item)
# for item in range(5, 10, 2):
#     print(item)

# #Exercise: calculate the total cost of all the items in a shopping cart
# prices = [10,20,30]
# total = 0
# # check each item in the prices list and then add their costs to total
# for item in prices:
#     total += int(item)
# print(f"Total: ${total}")

# # Nested Loops
# #generate coordinates using nested loops
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# # Problem: take a list of values and use it via a for loop to draw n number of x's len number of times
# numbers = [5,2,5,2,2]
# string = ''
# for num in numbers:
#     x_count = num
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

# # Lists
# names = ['john', 'bob', 'mosh', 'sarah', 'mary']
# # grabbing item in list via index
# print(names[0])
# print(names[-2])
# print(names[2:])
# print(names[-2:0:-1])
# # changing list
# names[0] = 'bob'
# print(names)

# # exercise: find the largest number in a list
# numbers = [0,3,43,43,2,2,3,43,234,5,43,664,3,1231,23]
# largest_num = 0
# index = 0
# for num in numbers:
#     if num > largest_num:
#         largest_num = num
#         l_num_index = index
#     index+=1
# print(f"The largest number is {largest_num} and is located at numbers[{l_num_index}].")

# 2 dimensional Lists
matrix = [
    # remember your comma's outside the seperate lists
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# # how to grab our data from the matrix
# # matrix[0][1] = 20
# # print(matrix[0][1])
# # print(matrix)
# # for row in matrix:
# #     for item in row:
# #         print(item)

# # List Methods
# numbers = [5,5,2,1,7,4]
# #count number of occurences of a value
# print(numbers.count(5))
# #append a value to the end of the list
# numbers.append(20)
# print(numbers)
# #at index insert value
# numbers.insert(0,10)
# print(numbers)
# #remove first occurrence of value
# numbers.remove(5)
# print(numbers)
# # remove the last item in the list
# numbers.pop()
# print(numbers)
# # returns the index of the first occurence of the item
# print(numbers.index(7))
# #clear will empty it out
# #check for item in list.. returns a boolean value so there is no error if it isn't in the lsit
# print(50 in numbers)
# #sort the list
# numbers.sort()
# print(numbers)
# #reverse the list
# numbers.reverse()
# print(numbers)
# # make a copy of the list... changes made to first list afterwords do not affect the copy
# numbers2 = numbers.copy()
# print(numbers2)
# # clear the list
# numbers.clear()
# print(numbers)

# Exercise: Remove duplicates from a list
# My bad solution
# list1 = [1,2,1,4,3,4,3,7,9,10,12,12,13,14,2,3,1,10,4,13,12,1,6,3]
# list2 = []
# list1.sort()
# for value in list1:
#     if value in list2:
#         print("value already exists")
#     else:
#         list2.append(value)
#         print(list2)

# # Tuples : similar to lists except that you cannot modify them
# # Parenthesis make it a tuple
# numbers = (1,2,3)
# #count to count occurences of item in tuple
# print(numbers.count(2))
# #index to get index
# print(numbers.index(2))
#
# # Unpacking
# #tuple coordinates
# coordinates = (1, 2, 3)
# coordinates[0]  * coordinates[1] * coordinates[2]
# #store in seperate values to reduce clutter later on
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# #unpacking example to massively reduce clutter.. works with lists and tuples
# x,y,z = coordinates
# print( x ,y, z)

# # Dictionaries: store key value pairs
# #dictionary example
# customer = {
#     "name": "John Smith",
#     "Age": 30,
#     "is_verified": True
# }
# #update values
# customer["name"] = "Jack Smith"
# #print the whole dictionary
# print(customer)
# #print a selection from the dictionary.. use the tags... this is case sensitive
# print(customer["name"])
# #get method to grab key without having to worry about error if you try to grab a key that doesn't exist
# print(customer.get("birthday"))
# #can add default in case there is nothing for the key yet
# print(customer.get("birthday", "Jan 1 1980"))

# # Exercise: convert numberic phone number to words
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3":"Three",
#     "4": "Four"
# }
# phone_number_mapped = ''
# number = input("type your phone number without dashes. ex:5673138241: ")
# for ch in number:
#     phone_number_mapped+= digits_mapping.get(ch, "Not in dictionary") + " "
# print(phone_number_mapped)

# #Emoji Converter: using dictionaries
# message = input(">")
# #call split message to split string into seperate words and return a list
# words = message.split(" ")
# print(words)
# emojis = {
#     ":)": "😀",
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# # Functions
# #container for a few lines of codes that perform a specific task
# def greet_user():
#     print('Hi there!')
#     print('Welcome aboard')
# print("Start")
# greet_user()
# print('finish')

# #Parameters... we can set parameters for functions to use and become more reusable...
# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}!")
#     print("Welcome aboard")
# greet_user("John", "Smith")
# greet_user("Mary", "Smith")

# #Keyword Arguments...generally we are using positional arguments however keyword arguments can help to make things clearer
# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}!")
#     print("Welcome aboard")
# #using key words to tell python which parameter argument is which
# #if it isn't easy to guess what a value represents then it's worth using keywords
# #example: calc+cost(total=5-, shipping=5, discount=.1
# greet_user(last_name="Smith", first_name="John")
# #final note: keyword args always come after positional arguments otherwise it will throw an error
# greet_user("John", last_name="Smith")

# #return statement
# def square(number):
#     return number * number
# result = square(3)
# print(result)
# #can also just print the function call
# print(square(3))
# #what if we dont return anything?
# def square(number):
#     number*number
# print(square(3))
# #we get a return value of None. an object representing the absence of a value

# #creating a reusable function
# def emoji_converter(message):
#     #call split message to split string into seperate words and return a list
#     words = message.split(" ")
#     #print(words)
#     emojis = {
#         ":)": "😀",
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
# message = input(">")
# print(emoji_converter(message))
# sentence = "Hi there :)"
# print(emoji_converter(sentence))

# #Exceptions... aka handling errors
# #Try Except...
# try:
#     Age = int(input('Age: '))
#     income = 20000
#     risk = income / Age
#     print(Age)
# #there is also an error that can occur when you try to divide by zero... thus
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# # One situation we can run into is Value errors where an invalid argument is passed such as string characters being passed for an int
# except ValueError:
#     print('Invalid value')

# #Comments
# #Use comments to explain WHYS and HOWS... don't be repetitive or unnecessary though
# print("Sky is blue")

# #Classes:used to define new types to model real concepts
# numbers = [1,2,3]
# #Pascal naming convention: Use Caps when naming classes and dont use underlines just keep capitalizing first letter of words
# class Point:
#     #now we define functions/methods
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# point2 = Point()
# point1.draw()
# print(point1.x)
# #will give an error because it doesn't have its own x
# print(point2.x)

# #Constructors...function that gets called at the time of creating an object
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     #now we define functions/methods
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point(10,20)
# point1.x  = 11
# print(point1.x)

# #Exercise: make a Person class with a name variable and a talk method
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self,name):
#         print(f"Hello good sir. My name is {self.name}. What would you like to talk about today?")
#
#
# person = Person("Bob")
# print(person.name)
# person.talk(person.name)

# #Inheritence: DRY-dont repeat yourself
# class Mammal:
#     def walk(self):
#         print("walk")
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark")
#     #can use pass to make python ignore for the time being
#     #pass
# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying you")
#
# cat1 = Cat()
# cat1.be_annoying()
#     #pass
#
# dog1 = Dog()
# dog1.walk()

# Modules... we refer to each file as a module which lets us reuse our code
# #we import module files to reuse our methods classes etc
# # def lbs_to_kg(weight):
# #     return weight * 0.45
# #
# #
# # def kg_to_lbs(weight):
# #     return weight / 0.45
# # ### Now even when the code is commented out here it will still be usable because we are grabbing it from another file
# # and with the import converters   up at the top of the file we can do this
# print(converters.kg_to_lbs(70))
#
# #if we want to only import a specific function we can do " from converters import kg_to_lbs"
# #then we can simply call the function normally without the converters tag
# print(kg_to_lbs(100))
# # as seen above

# #Exercise: Write a function that takes a list of numbers and finds the largest number in it
# # then put it into a seperate module and import it back into here and run it
# numeric_list = [1,4,3,2,5,232,52,232,2,3,323234,42,42323,24324,234324,234234,234,23423412423,4234234,2423]
# print(find_max((numeric_list)))
# print(max(numeric_list))

# Packages..container for multiple modules.. aka folders/directories
# We made a new package with a module in it so...
# #verbose
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()
# #get specific function
# from ecommerce.shipping import calc_shipping
# calc_shipping()
# # get the module
# from ecommerce import shipping
# shipping.calc_shipping()

# #Random values
# #python 3 module index to get the list of all python 3 modules ***********************************************
#
# import random
# for i in range(3):
#     print(random.random())
# for i in range(3):
#     print(random.randint(10,20))
# members = ["doyle", "bob", "Tyty"]
# #randomly pulls a member form the list
# leader = random.choice(members)
# print(leader)

# Exercise
'''
Create a class called Dice
    give it a method called roll() and return a tuple of two random values
'''
# import random
#
#
# class Dice:
#
#     def roll(self):
#         val1 = random.randint(1, 6)
#         val2 = random.randint(1, 6)
#         dice_vals = (val1, val2)
#         return dice_vals
#         #note another way you can return a tuple is via: return val1, val2 : no need for parenthesis either
#
#
# dice = Dice()
# print(dice.roll())

# #files and directories
# from pathlib import Path
# # Absolute Path
# # C:\Program Files\Microsoft\...
# # Relative Path
# path = Path("ecommerce")
# print(path.exists())
# # Make a new directory
# path1=Path("emails")
# #note even if we print it, the directory will still be made however, the print statement will return None because
# # upon printing, nothing was there
# print(path1.mkdir())
# # Deleting directories, returns None again
# print(path1.rmdir())

# #iterate over all the spreadsheets in a directory, open them and process them..
# from pathlib import Path
# path = Path()
# #search everything in the current path
# print(path.glob('*'))
# #search only the files in the current directory .
# print(path.glob('*.*'))
# # search only .py files
# print(path.glob('*.py'))
# #go through all the files and print them out
# for file in path.glob('*'):
#     print(file)
bob  =[2]
# Pypi and Pip: search for modules that others have made