# variables - This is a single line comment that starts with #
# Python download -> libraries, files, py software......PVM, IDLE

x = 2 # x is the variable that is assigned a value of 2 which is of type integer.

# dynamically typed language - interpreter based and not compiler based.

print(x) # 2

# print(y) - NameError: name 'y' is not defined. This happens becoz we have to first define the variable and so far in this file there is no variable y

y = 4.49
print(y) # 4.49 

print(type(x)) # <class 'int'>

print(type(y)) # class float  <class 'float'>

# string -  characters, is nothing but text
string_variable = 'ThinkPythonAI' 
print(string_variable)
print(type(string_variable)) # <class 'str'>


a = '2'
print(a) # error......2......
print(type(a))
#print(a+x) # 4........error.....22..... # can only concatenate str (not "int") to str


# complex no - real no + imaginary no eg 4 + 5i (this is per maths)
x = 5+10j # j represents the imaginary part whcih in math is defined as the i part.

print(x) # (5+10j)
print(type(x)) # <class 'complex'>


a=10 
b=100
a=15

print(a) # error....15....10


print("======type casting========")
a=4.89
print(a)
print(type(a)) # class float
print(int(a))  # 4 ----> we are just asking the interpreter to print the integer part of a
print(a) # 4.89.......4......
print("implicit type casting")
a=int(a)
print("explicit type casting - when you explicity change the type of the value and reassign it to the same varaible")
print(a) # 4

print(float(a)) # 4.0

str1="Sudeep"
print(int(str1)) # error...... S u d e e p.......6.... ->           ####ValueError: invalid literal for int() with base 10: 'Sudeep'

'''
This is a multi line comment, this is the first line of my comment,
This is the second line of my comment
This is the third line of my comment
This is the fourth line of my comment
'''




