#---- IMPORTING MODULES ----
import os
import datetime
import random
import requests
import pyodbc



#---- VARIABLES AND DATA TYPES ----

number = 10
name = "John"
pi = 3.14159
boolean = True
list = [1, 2, 3]
dictionary = {'a': 1, 'b': 2}



#---- CONTROL STRUCTURES ----

x = 10

if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is exactly 10")
elif x > 5:
    print("x is greater than 5 but less than 10")
else:
    print("x is 5 or less")


#---------------------------------------------------------------------


#---- LOOPS ----

#---- ITERATE OVER A LIST ----
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)


#---- ITERATE OVER STRING ----
for char in "Hello":
    print(char)


#---- ITERATE WITH A RANGE ----
for i in range(5):
    print(i)    


#---- NESTED LOOP ----
for i in range(3):
    for j in range(i + 1):
        print(f'({i}, {j})')


#---- ITERATE OVER DICTIOARY ----
person = {'name': 'John', 'age': 30, 'city': 'London'}

#-- 1 --
for key in person:
    print(key, person[key])

#-- 2 --
for key, value in person.items():
    print(key, value)


#---------------------------------------------------------------------

#---- COUNTING UP ----
count = 0
while count < 5:
    print(count)
    count += 1


#---- COUNTDOWN ----

x = 10
while x > 0:
    print("Countdown:", x)
    x -= 1    


#---- FUNCTIONS ----

def greet(name):
    return f"Hello, {name}!"
print(greet("Jane"))  # Output: Hello, Jane!


def add_numbers(a, b):
    return a + b
result = add_numbers(3, 5)
print(result)  # Output: 8


#---------------------------------------------------------------------

#---- INPUT AND OUTPUT ----
name = input("Enter your name: ")
print("Hello,", name)


#---- CREATE FILE ----
# EG HTML FILE
html_content = "<html><body>"
html_content += "<p>Hello</p>"
html_content += "</body></html>"

with open("examplefolder/example.html", "w") as file:
    file.write(html_content)



def madeupfunction():
    pass

#---- EXCEPTION HANDLING ----
try:
    madeupfunction()
except:
    print("Your Function Failed!")



#---- CLASSES ----
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 30)
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.


#----------------------------------------------------------------------------------
