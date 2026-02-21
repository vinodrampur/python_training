'''
Tuples are another type of datatypes that are heterogenous and can contain a combination of other DT's as well, and sperated by a comma ','
Tuples can have numbers, strings, floats, etc so a combination of all other DT's under one variable called tuple_variable.
tuples are iterables.
Tuples are "immutable" object, they are ordered and they allow duplicates. This means they CANNOT Change the values.
Tuples can be defined as 2 types:
a. var = ()
b. tuple() internal tuple function
'''

tup_eg=(1,2,3,4,5,5,4,4.89,1,1)
print(tup_eg)
print(type(tup_eg))

print(tup_eg.count(1))
print(tup_eg.index(5))

#tup_eg[4] = 100 # TypeError: 'tuple' object does not support item assignment - we cannot modify a value inside a tuple
#print(tup_eg)


# packing and unpacking of a tuple.
num=1,2,3  # packing of values inside a tuple.  This is internally stored as num=(1,2,3) which is a tuple.


print(num) # (1, 2, 3)
print(type(num))
print(num[1])

num=1,2
print(type(num))

num=1
print(num) # 1
print(type(num))  # int.......tuple.... 


num=1,
print(num) # error..... int.....tuple....  #(1,) 
# this is a very special case in python which is called a SINGLE element tuple.
print(type(num))

#print(num[1]) # space......error....

employee = ("john" , 35, 100.89, 'residentatial', 'm' , ["python", "C++", "JAVA"]) 

print(employee[-1][-1]) # JAVA
print(type(employee))

tmp=employee[-1]
tmp.append("Ruby")

print(tmp)
print(employee)




