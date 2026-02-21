'''
Everything in Python is an object!

A collection of characters is a string.
how do we define them
a. ' '
b. " "
c. ''' '''
d. str() - inbuilt string function to define a string.

CPython

'''

name = '''Ankit is a trainer for "Python" classes and is one of the few trainer's 
    and also teaches "AI" '''
print(name)

print(type(name)) # <class 'str'>

str1 = "ThinkPythonAI"

print(str1.split("P")) # ['Think', 'ythonAI']


mob_num = "123 456 6789"
print(mob_num) # error.....int......string...
print(type(mob_num))


str1 = "All is good here in ThinkPythonAI"
print(str1.find("good"))











