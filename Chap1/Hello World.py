# Variable #
# age = 30 (int)
# name = "Shivansh" (String)
# marks = 98.5 (float)

# print to console
# print(30)

# get remainder of a division
#
#integer_division = 13//5 # // ----> // means round off
# #print(12%8)         ----> // modulus finds remainder

# name = "Shivansh"
# print(f"your name is {name}")

# greetings = "How are you? {}? your age is {}."
# final_greetings = greetings.format("shivansh", "14")  -----> str w/ formatting.

#  Getting input from user
# name = input("please type your name: ")
# age = input("please type your age: ")
# print(f"Hi {name}, Your age is {age}.")

# Booleans #
# isTrue = True

# and & or keywords #
# marks = int(input("Enter your Marks: "))
# eligible_for_schlarship = marks > 90 and marks < 100
# print(f"{eligible_for_schlarship}")

# age = int(input("Enter your age: "))
# is_working = age >= 18 or age <= 65
# print(is_working)

# List #
# friend = ["Aaryan", "Smarth", "Arjun"]
# # print(friend[0])
# print(len(friend))

# friends = [
#     ["Ram", 40],
#     ["Raghav", 10],
#     ["Ranveer", 28]
# ]
# print(friends[2][1])

# # Adding to a list #
# friends = [
#     ["Ram", 40],
#     ["Raghav", 10],
#     ["Ranveer", 28]
# ]
#
# friends.append(["Ram", 20])
# friends.remove(["Ram", 20])

# Tuples #
# friends = {"Ram", "Bob"}
# friends.add("Aaryan")
# print(friends)

# Sets #
# art_friends = {"Ram", "Mohan", "Jen"}
# science_friends = {"Jen", "Charlie"}
#
# art_but_not_sci = art_friends.difference(science_friends)
# sci_but_not_art = science_friends.difference(art_friends)
# not_common = art_friends.symmetric_difference(science_friends)
# in_both = art_friends.intersection(science_friends)
#
# print(in_both)
# print(not_common)
# print(sci_but_not_art)
# print(art_but_not_sci)

# Dictonary #

# friend_marks = {"Aaryan": 30, "Arjun": 31, "Pixlriffs": 365}
# friend_marks["Shivansh"] = 30

# friends = [("Pixlriffs", 30), ("Wattles", 36), ("Xisumavoid", 40)]
# friends_dict = dict(friends)
# print(friends_dict)

# Sum & Lengths #
# grades = [80, 75, 90, 100]
#
# total_grades = sum(grades)
# length = len(grades)
#
# average = total_grades/length
# print(average)

# joining a list #
# friends = ["Rolf", "Anne", "Charlie"]
# comma_separated = ", ".join(friends)
# print(f"my friends are {comma_separated}")