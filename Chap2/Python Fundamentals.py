# 1 #
# If Statement #
# required_name = "Shivansh"
# user_name = input("Enter your name: ")
#
# if(user_name == required_name):
#     print(f"Welcome {required_name}!")
# else:
#     print(f"Hello Stranger!")
# 2 #
# using if in Comparison with a str and list #
# friends = ["Aaryan", "Arjun", "Smarth", "Ankit"]
# teachers = ["Sita", "Vinod", "Pramod", "Kin"]
#
# username = input("Enter your name: ")
#
# if username in friends:
#     print("hello friend!")
# elif username in teachers:
#     print("Hello teacher!")
# else:
#     print("Hello Stranger!")

# 3 #
# Loops #
# While Loop #
# is_learning = True
#
# while is_learning:
#     print("You're Learning!")
#     user_input = input("Are you still learning? ")
#     is_learning = user_input == "Yes"
# For loops #

# for i in range(10): #range ----> makes a list with a number of elements.
#     print(f"{i}")

# range #
# for i in range(1, 10):
#     print(i)             #-------> prints numbers from 1 to 10

#
# for i in range(1, 10, 2):
#     print(i)     #------> prints odd numbers(with gap of 2) between the given range
#

# Example "Marks Scored in a  test" #
# students = [
#     {"name": "Aaryan", "grade": 36},
#     {"name": "Shivansh", "grade": 39}
# ]
#
# for student in students:
#     name = student["name"]
#     grade = student["grade"]
#
#     print(f"{name} has scored {grade}")

# Destructuring syntax #
# currencies = 74.21, 102.99
# usd, sterling_pound = currencies
#
# print("1 usd is " + str(usd) + ", 1 Sterling Pound is " + str(sterling_pound))

# friends = [("Aaryan", 13), ("Ankit", 12), ("Smarth", 14)]
#
# for name, age in friends:
#     print(f"name is {name} and age is {age}")

# Iteration in Dict #

# friend_ages = {"Rolf": (20, 21),
#                "Anne": (31, 32),
#                "Charlie": (33, 34),
#                "Bob": (35, 36)
#                }

# for name in friend_ages:          |
#     print(f"name: {name}")        |
#                                   | ------> not iterated
# for age in friend_ages.values():  |
#     print(f"age: {age}")          |

# for name, age in friend_ages.items():
#     print(f"{name} is {age} years old.")

# for name, age in friend_ages.items():
#     n1 , n2 = age
#     print(n1)

# Break and Continue #
# pen = ["ok", "ok", "ok", "faulty", "ok"]

# for status in pen:
#     if status == "faulty":
#         print("faulty")
#         continue
#     print(f"The status of pen is {status}, sending it to customer!")

# else with loops #

# pen = ["ok", "ok", "ok", "ok"]
#
# for status in pen:
#     if status == "faulty":
#         print("faulty")
#         continue
#     print(f"The status of pen is {status}, sending it to customer!")
# else:
#     print(f"no errors!")

# if no breaks were done during the loop then
# we go to the else statement of we skip the
# else statement

# Console log #
# The status of pen is ok, sending it to customer!
# The status of pen is ok, sending it to customer!
# The status of pen is ok, sending it to customer!
# no errors! ----> came from else

# Getting Prime Numbers # exercise
#
# print("Welcome to Prime numbers finder!")
# prime_number = range(int(input("please enter minimum number: ")),
#                      int(input("please enter maximum number: ")))
#
# for n in prime_number:
#
#     if n == 1:
#         continue
#
#     for x in range(2, n):
#         if n % x == 0:
#             #print(f"{n} can be written as {x} * {n//x}")
#             break
#     else:
#         print(f"{n} is a prime number!")

# Slicing a List #
# friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
#
# print(friends[1:5]) #------> from 1st element to 5th element

# List Comprehension #

# numbers = [1, 5, 10]              |
# doubled_numbers = []              |
#                                   |
# for x in numbers:                 | ----> dumb
#     doubled_numbers.append(x * 2) |
#                                   |
# print(doubled_numbers)            |

# numbers = [1, 5, 10]
# doubled_numbers = [number * 2 for number in numbers]
# print(doubled_numbers)

# friend ages in string using list comprehension #
# friend_ages = [22, 31, 35, 37]
# friend_ages_str = [str(age) for age in friend_ages]
# print(friend_ages_str)

# get a lower case name #
# name = ["Rolf", "Jen", "Bob"]
# name_lowercase = [str(n).lower() for n in name]
# print(name_lowercase)

#  List Comprehension with conditional #
# ages = [22, 35, 27, 21, 20]
# odd_age = [age for age in ages if age % 2 == 1]
# print(odd_age)

# checking if a name is in both lists #
# friends = ["Rolf", "ruth", "Charlie", "jen"]
# guests = ["Jose", "bob", "rolf", "charlie", "michael"]
#
# friends_lower = [f.lower() for f in friends]
#
# present_friends = [
#     name for name in guests if name.lower() in friends_lower
# ]
#
# title_present = [print(t.title()) for t in present_friends]

# Set and Dict comprehension #

# friends = ["Rolf", "ruth", "Charlie", "jen"]
# guests = ["Jose", "bob", "rolf", "charlie", "michael"]
#
# friends_lower = {n.lower() for n in friends}
# guests_lower = {n.lower() for n in guests}
#
# present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}
#
# print(present_friends)            same as comprehension for str

# friends = ["Rolf", "Bob", "Jen", "Anne"]
# time_last_seen = [5, 6, 2, 9]
#
# long_time = {
#     friends[i] : time_last_seen[i]
#     for i in range(len(friends))
#     if time_last_seen[i] > 5
# }
# print(long_time)

# zip function #

# friends = ["Rolf", "Bob", "Jen", "Anne"]
# time_last_seen = [5, 6, 2, 9]
#
# friends_last_seen = dict(zip(friends, time_last_seen))
#
# print(friends_last_seen)

# Enumrate function #
# friends = ["Rolf", "John", "Anne"]
#
# print(list(enumerate(friends)))
# print(dict(enumerate(friends)))
#
# for counter, friends in enumerate(friends):
#     print(f"{counter}. {friends}")

# Functions #
# def greet():
#     name = input("Please enter your name: ")
#     final_name = name.title()
#     print(f"Hello {final_name}!")
#
# greet()

# Functions with parameters #
# def greet(name):
#     print(f"Hello, {name}!")
#
# input_name = str(input("Please enter your name: ")).title()
# greet(input_name)

# return #
# def multiply(x, y):
#     total = x * y
#     return total
#
#
# print(multiply(20, 5))

# Default values for parameters #
# def multiply(x, y=2):
#     total = x * y
#     return total
#
#
# print(multiply(6)) //2 is taken  as default value of y

# Lambda Function #
# multiply = lambda x, y: x * y
#
# print(multiply(5, 6))

# Average of students using lambda function #

# average = lambda sequence: sum(sequence)/len(sequence)
#
# students = [
#     {"name": "Rolf", "grades":(67, 90, 95, 100)},
#     {"name": "Bob", "grades":(56, 78, 80, 95)},
#     {"name": "Jen", "grades":(98, 90, 95, 99)},
#     {"name": "Anne", "grades":(100, 100, 95, 100)},
# ]
#
# for s in students:
#     s_name = s["name"]
#     s_average = average(s["grades"])
#     print(f"{s_name} has a average of {s_average}.")

# First class functions #
# we can assign a fucnction to a variable
# and pass them in as argument to other
# functions

########## Dumb Way ################
# average = lambda seq: sum(seq)/len(seq)
# total = lambda seq: sum(seq)
# top = lambda  seq: max(seq)
#
# students = [
#     {"name": "Rolf", "grades": (67, 90, 95, 100)},
#     {"name": "Bob", "grades": (56, 78, 80, 95)},
#     {"name": "Jen", "grades": (98, 90, 95, 99)},
#     {"name": "Anne", "grades": (100, 100, 95, 100)},
# ]
#
# for s in students:
#     name = s["name"]
#     grades = s["grades"]
#
#     print(f"Student: {name}")
#     operation = input('Enter "average", "total" or "top": ')
#
#     if operation == "average":
#         print(average(grades))
#     elif operation == "total":
#         print(total(grades))
#     elif operation == "top":
#         print(top(grades))
#     else:
#         print("invalid argument")

######### Neat Way ###########

# average = lambda seq: sum(seq)/len(seq)
# total = lambda seq: sum(seq)
# top = lambda seq: max(seq)
#
# operations = {
#     "average": average,
#     "total": total,
#     "top": top
# }
#
# students = [
#     {"name": "Rolf", "grades": (67, 90, 95, 100)},
#     {"name": "Bob", "grades": (56, 78, 80, 95)},
#     {"name": "Jen", "grades": (98, 90, 95, 99)},
#     {"name": "Anne", "grades": (100, 100, 95, 100)},
# ]
#
# for s in students:
#     name = s["name"]
#     grades = s["grades"]
#
#     print(f"Student: {name}")
#     operation = input('Enter "average", "total" or "top": ')
#
#     operation_function = operations[operation]
#     print(operation_function(grades))