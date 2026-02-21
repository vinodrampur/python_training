'''
its basically a block of code that you can use and "re-use" multiple times.
you write the logic once but you can call the function many times.
eg add two nos
a=12
b=15
print(a+b)
x=13
y=18
print(x+y)
a1=22
b1=115
print(a1+b1)

type of functions:
print(), type(), int() etc - inbuilt functions
user-defined functions
lambda functions - v v popular and int fav? why? becoz they are very very efficient way of writing the code
magic methods or dunder methods or super methods - eg __add__  - when we write functions inside a class they are caled methods.

syntax :
every func has 2 main things:
a. function definition
def function_name(param1,param2,...paramn):
    <block of code of logic inside that function>
    <optional return>
    <recommended as per coding standards is not more than 60 lines>

b. function call
function_name(arg1,arg2,...argn)

imp: function def has to be written before the function call.
'''

# function definition - addition of two numbers. we donly define the funciton once.
def add_two_nos(a,b):
    print(a+b)
    #return None - internally no return statement is implied as None
    #return(a+b)


add_two_nos(2,5)
#add_two_nos(2,5)# will still be a diff memory of its own
add_two_nos(13,18)# 31
add_two_nos(21,51)

# function call

#print(add_two_nos(2,5))#7
#res=add_two_nos(2,5) # assigning the function to a variable

#print(res**2)

print("======================")


def add_two_nos(a,b):
    print(a+b)

add_two_nos(2,5)
add_two_nos("Think","Python") #error... no error...concatenate....

'''
def add_two_nos(int a, int b)
def add_two_nos(str a, str b)

'''

print("=========")
def add_two_nos1(a,b):
    # implementation
    print(a*10)
    print(str(a)+b)
    print("hello"+ b)

add_two_nos1(5,"think")

# Fucntions are a first class objects.