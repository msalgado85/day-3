# # #order of execution in python 
# # print("hello world")
# # #things are surrounded by either double or single quotes, you must be consistent the starting quote mark should be the end "" and ''
# # print("order of execution")
# # print("in python")
# # print("*"*20)

# # #variables are container for your code 
# # price = 10 #intenger variable
# # name = 'john' #string variable
# # rating = 4.9 #float variable
# # is_published = True #boolean variable
# # #start all varibles with a lowercase letter, to separate words use underscore, or camel case if you want to start with a capital letter
# # playerBulls = 'micheal jordan'
# # #concatentation to join variables in a sentence  in the following code it is '+'
# # #() converts a Number inot a a string
# # print(name + 'is a basket ball player')
# # print(name + 'haws a rating of' + str(rating))
# # print('the price of the book is' + str(price))

# #getting input from the user
# # name = input('what is your name? ')
# # age = input('What is your age? ')
# # print('Hello ' + name + ' you are ' + age + 'years old ')

# #ask two questions from the usert 
# #persons name and fav color 
# name = input('what is your name? ')
# color = input('What is your fav color? ')
# print(name + " likes " + color)

# # Description: This file is for the second day of the python workshop


# # create variables for the following :
# # rule: set variables against margin
# # 1. age
# age = 25
# # 2. name
# name ="John"
# # 3. song
# song= "Happy Birthday"
# # 4. food
# food ="oranges"
# # 5. number
# number="12"
# priceOfMovie= 10.99
# print(f"({name} is {age} years old.")

# # print (f"Once upon a time, there was a (age) old coder named (name)")
# # print ("(name) liked to hum the song (song) while coding. It was so annoying that their teammates would throw food (food) until (name) would stop siinging.")
# # #now include the variables you just made print in the following...

# print('''Once upon a time, there was a {age} old coder named {name}.
# {name} liked to hum the song {song} while coding. It was so annoying that their teammates would
# throw {food} until {name} would stop singing.
# Still, {name} was the best coder on the team and could write {number} lines of code every day.
# Maybe {song} was {name}'s secret power?
# No one will ever know.''')

# # f string interpolation is a way to format strings in

# # What is syntax ? What is an algorithm?
# # Is a way of writing code

# # what is a variable? What is a string?
# # It holds data
# # name = "John" 
# # age = is undefinedd because it has no value

# # strings are nothing but plain text

# # what does this do?
# print("Giraffe \n academy")
# # /n creates a new line
# print("Giraffe \t academy")
# # \t makes a new tab

# # or this
# phrase = "python learning"
# print(phrase + "is cool")
# #this is called concatnation or string interpolation. 

# #what does the + sign do? What is it called?
# # the plus sign adds the subjects together

# #what if I wanted to get the length of a phrase?
# phrase = str(phrase)

# print (f'the length of the declaration is'{len(declarationOfIndependence)}')
      
# declarationOfIndependence=""
# print("The length of the phrase" len (phrase))

# declarationOfIndependence = "When, in the course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume, among the powers of the earth, the separate and equal station to which the laws of nature and of nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation."
# print(len(declarationOfIndependence))
# print("the lenghth of the declaration is"+ len(declarationOfIndependence))
#what if I wanted to make the letters in the variable upper case or lower?

# new_phrase = "welcome to day 2 part 3"
# print(len(new_phrase))
# print(new_phrase.upper())
# # .upper is a method that makes the string all upper case
# # parentheses are used to call mathods
# print(new_phrase. lower())
# # .lower is a method that makes the string all lower case

# # what if I wanted to check and see if the phrase was all lowercase

# print(new_phrase.islower())

# # what if I wanted to get one letter of the phrase
# print(new_phrase[0])
# print(new_phrase [1])
# print(new_phrase [11])
# print(new_phrase [20])
# # you can count but [-1] a;so gives you the last character
# print(new_phrase [-1])

# # The names you use when creating these labels need to follow a few rules:
# # 1. Names can not start with a number.
# # 2. There can be no spaces in the name, use _ instead.
# # 3. Can't use any of these symbols :'",<>/?|()!@#$%^&*~-+
# # 4. It's considered best practice (PEP8) that names are lowercase.
# # 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase
# # letter eye) as single character variable names.



# # Working with numbers bold text
# # We'll learn about the following topics:
# # 1. Types of Numbers in Python
# # 2. Basic Arithmetic
# # 3. Differences between classic division and floor division


# # # Addition
# # ('+'):Sum of numbers
# print(2 + 2)
# # # Subtraction
# print(2 - 5)
# # # Multiplication
# print(2 * 3)
# # # Division
# print(10 / 2)
# # # Modulus
# print(10 % 3)
# # # Exponentiation
# print(2 ** 3)
# # # Floor Division
# print(10 // 3)
# # Order of Operations followed in Python

# # You can use parentheses to specify the order in which you want operations to be performed.

# #to do more you need to import special math libraries from python
# #from math import *
# #this goes out and grabs some different math functions we can use
# #floor method
# #ceil method
# #sqrt method
# from math import * #import everything
# print(floor(95.76666))
# print(ceil(98.3333))
# print(sqrt(54))


# Python has various "types" of numbers (numeric literals).
# 1. We'll mainly focus on integers and floating point numbers. Integers are just whole numbers,
# positive or negative. For example: 2 and -2 are examples of integers.
# 2. Floating point numbers in Python are notable because they have a decimal point in them, or
# use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of
# floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating
# point number in Python.



# challenge exerces... 
#create a program that asks for the user's name and age and then prints out the user's name and age

# create a program that asks for the user's name and then prints out the user's name in all caps

# create a program that asks for the user's name and then prints out the user's name in all lower case

# create a program that asks for price and then prints out the price with a 10% discount

# Given the phrase "Hancock High School", perform the following operations:
# Print the phrase with a newline character to separate "Hancock" and "High" and "School".
# Concatenate the phrase with " is cool", and print the result.
# Print the length of the phrase.
# Convert and print the phrase in uppercase and lowercase.
# Check if the phrase is all lower or all upper and print the result.
# Print the first and the last letter of the phrase.

avg_grade = int(input("What is your average grade? "))
if avg_grade>=85:
    print("you are awarded honor roll! congrats! ")
else:
    print("You do not qualify for honor roll!")
extra_activities = int(input("how many extra curriculars are you in? "))
if extra_activities >=3:
    print("You have been recognized for high involvement!")
else:
    print("Sorry! You have not been recognized for high involvement")