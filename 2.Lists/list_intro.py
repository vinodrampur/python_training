'''
lists are another type of datatypes that are heterogenous and can contain a combination of other DT's as well, and sperated by a comma ','
lists can have numbers, strings, floats, etc so a combination of all other DT's under one variable called list_variable.
Lists are iterables.
Lists are mutable object, they are ordered and they allow duplicates.
Lists can be defined as 2 types:
a. var = []
b. list() internal list function
'''

'''
Coding standards - NOT a syntax requirement. Code maintainbility
as per the recommendations.
1. Rule1 - the name of the variables, and functions, and classes all should be meaninful and telling something about those
for eg
x=10 is a very bad way of coding
var_x=10
Rule2. Naming conventions: there are two types: Choose one and m.importantly STICK to that.
a. var_listof_nos - this is the most widely used.
b. varListofNos

fucntions and classes should have a comment above them - which details in plain english whatr the function or class is supposed to do.
Very bad
def fn(a,b):
    print(a+b)
rather

# Below is a functioin to add two numbers.
def add_two_nos(a,b):
    print(a+b)
'''

listx=[1,2,3,4]
print(listx)
print(type(listx)) # <class 'list'>

list_var=[1,2,3,4,1,3,4.89,'ankit',4+5j]
print(list_var) # [1, 2, 3, 4, 1, 3, 4.89, 'ankit', (4+5j)]
print(list_var[4]) # 1 ----> [1, 2, 3, 4, 1, 3, 4.89, 'ankit', (4+5j)][4] ---> 1
