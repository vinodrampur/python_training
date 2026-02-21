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

# mutability - changeable. add, modify, and/or delete that means as a DT we are mutable or chaneable.
# listx = [] # empty list - this is not required in python but good to know that this is an empty list. 

print(list_var[2:7]) # 3,4,1,3......3....3,4,1.....3,4,1,3,4.89   ---> [3, 4, 1, 3, 4.89]

employee = ["john" , 35, 100.89, 'residentatial', 'm' ]
print("The employee's name is :", employee[0], " and he makes an hourly rate of :", employee[2])


# mutability

listx = [1,2,3,4,5]

print("======before append listx is =========")
print(listx)
listx.append(8)
print("======after the append listx is =========")
print(listx) # we are able to add an element to an existing list

# [1, 2, 3, 4, 5, 8]
listx[2] = 100
print(listx) # [1, 2, 100, 4, 5, 8] - so modifiable

# [1, 2, 100, 4, 5, 8]
# pop() - removes the items in LIFO fashion. 

listx.pop()
print(listx) # [1, 2, 100, 4, 5] - delete is possible


for i in listx:
    print(i)

#[1, 2, 100, 4, 5]

listx.pop(2) # removes 100
print(listx)
#[1, 2, 4, 5]
#listx[2] = 90




listx = [1,2,3,1,2,3,1,1,1,1]
print(listx.count(1))

print(listx.index(1)) # 0
print(listx.index(1,1,7)) # 3

# nested lists -> lists whithin lists

employee = ["john" , 35, 100.89, 'residentatial', 'm' , ["python", "C++", "JAVA",]]

# C++ [5][1], [5][-2]....+

print("The employee's name is :", employee[0], " and he makes an hourly rate of :", employee[2], " and his coding knowledge is :", employee[5], "and his best coding lang is:", employee[5][-2] ) # first tep is employee[5] ---> ["python", "C++", "JAVA"][-2] ---> C++. employee[5][-2] ---> C++[1]

print(employee[5][-2][1])

print(employee[-1][-2][1])

