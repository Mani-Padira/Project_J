#Date : 2025-03-24 Day 1

#Variables in Python

x = 5
y = "John"
# we cahnge the value of y
y = "Sally"
print(x)
print(y)
# data types can also be specified
a = str(3)
b = int(3)
c = float(3.0)
# Type of the variable can be checked using type()
print(type(a))
# Assigning multiple values to multiple variables
d, e, f, g = 1, 2.0, "Hello", "World"
# print with formatting
print(f"Hello {y}")

# Data types in Python
# Python Numeric Datatypes
num1 = 5 # int
num2 = 0.3 # float
num3 = 6 + 7j # complex
print(type(num1))
print(type(num2))
print(type(num3))
# Python Sequence Datatypes
list1 = ["I", "am", "man"] # list is mutable
print(list1[1])
tuple1 = ("I", 9) # tuple is immutable
print(tuple1)
# create a set named student_id
student_id = {112, 114, 116, 118, 115}
# display student_id elements
print(student_id)
# display type of student_id
print(type(student_id))
# create a dictionary named capital_city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print(capital_city['Nepal'])
