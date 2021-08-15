# my_student = {
#     "name": "Shivansh Tiwari",
#     "grades": [90, 100, 86, 92, 100]
# }
#
# def average(student):
#     return sum(student["grades"]) / len(student["grades"])
#
# print(average(my_student)) #Data and function is dependent
#                            # fully my_student
#
#                            # Object stores a data and
#                            # does actions on that data


# class Student:
#     def __init__(self, new_name, new_grades): #Dunder func (Double Underscore)
#         self.name = new_name
#         self.grades = new_grades
#
#     def average(self):
#         return sum(self.grades) / len(self.grades)
#
# student_one = Student("Rolf Smith", [70, 88, 99, 90])
# student_two = Student("Aaryan", [80, 80, 80, 80])
#
# print(student_one.name) # Entities that store data and functions (method)
# print(student_two.average())

# Parameter naming in Python #
# class Movie:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
# Bharat = Movie("Bharat", 2007)
# print(Bharat.year)
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#
# class Garage:
#     def __init__(self):
#         self.cars = []
#
#     def __len__(self):
#         return len(self.cars)
#
#     def __getitem__(self, item):
#         return self.cars[item]
#
#
# cars = Garage()
# cars.cars.append("Grand i10")
# cars.cars.append("Honda City")
# print(cars.cars[1])