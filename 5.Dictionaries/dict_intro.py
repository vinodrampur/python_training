'''
Dictionary is a collection of datatypes that are heterogenous and can contain a combination of other DT's as well, and sperated by a comma ','
they are ordered and changeable * . Duplciate members are not allowed (*)
dict do not support indexing, they follow a "similar" mech as sets based on hashing.
defined as ={}
dict work on key:values pair

d1 = {k1:v1, k2:v2,........kn:vn}

keys - are STRICTLY immutable objects - meaning, int, tuples, strings, frozenset. they cannot be changed.
values - can be ANYTHING - meaning integers, strings, tuples, lists, sets, frozensets, dict. They can be changed.
'''

d1={1:"one",2:"Two"}

print(d1)

d2={
    1:"one",
    2:"Two",
    3:"three",
    4:"Four",
    5:"Five",
    6:"Six",
    6:"Seven",
    7:"Seven",
}

print(d2) # {1: 'one', 2: 'Two', 3: 'three'}

# you always and always need a key to get the corresponding value
print(d2[3])

print(d2[7])

# Values can be anything - like DO NOT CARE, meaning, lists, tuples int, strings, complex, sets,
# keys are immutable - int, tuples,frozenset,strings

# str1= 'Ankit'
# str1[3]="B"  # TypeError: 'str' object does not support item assignment
# print(str1)



# def a dict style data which will store all the student information for my Feb Prof batch 2026

students_of_feb_batch = {1:"Anand",2:"Anisha", 3:"Butchi", 4: "Sudhakar", 5:"Gopi", 6:"Nancy"}

print(students_of_feb_batch)
print(students_of_feb_batch[4])


students_of_feb_batch.update({8:"Sapphire"})
print(students_of_feb_batch)


d1={
    1:11,
    2:22,
}

d2={
    3:33,
    4:44,
}

#print(d1+d2)

'''
{
1:11,
2:22,
3:33,
4:44,
}
'''

d1.update(d2)
print(d1) # {1: 11, 2: 22, 3: 33, 4: 44}

# print(d1, end=" ")
# print(d2)
#print(d1 | d2)  shortcut to update.


d2={
    2:33,
    3:33,
}


d1.update(d2)
print(d1)

'''
{
1:11,
2:33,
3:33,
}
'''


d1={
    1:11,
    2:22,
    3:33,
    4:44,
}
d1.pop(2) #whole element based on the key......

print(d1)


d1.popitem() # LIFO
print(d1)



print("========")


car_dict_manf = {

    "brand": "Audi",
    "model": "q5",
    "year": 2025,
    "miles_on_car": 2000.80,
    "New": True, # boolean
}

print(car_dict_manf)

print(car_dict_manf.keys()) # dict_keys(['brand', 'model', 'year', 'miles_on_car', 'New'])
print(car_dict_manf.values()) # dict_values(['Audi', 'q5', 2025, 2000.8, True])
print(car_dict_manf.items()) # dict_items([('brand', 'Audi'), ('model', 'q5'), ('year', 2025), ('miles_on_car', 2000.8), ('New', True)])

# items - are stored as list of tuples with EXACTLY two elements.

print("=======imp=========")
a=(1,2,3,"ThinkPythonAI")

print(type(a))

d3={ 
    a:"First element",
    4:"Second element",
}


print (d3) # {(1, 2, 3, 'ThinkPythonAI'): 'First element', 4: 'Second element'}

print(d3[a])
print(d3[(1, 2, 3, 'ThinkPythonAI')])

'''
opt1-3

d3={ 
    a:"First element",
    4:"Second element",
}

opt2 -4
d3={

(1,2,3,"ThinkPythonAI"):"First element",
4: "SEcond element"
}

opt3:
error -3


'''



print("==========More==========")

employee = ("john" , 35, 100.89, 'residentatial', 'm' , ("python", "C++", "JAVA")) 

print(type(employee))

d4={
    employee: "Some value",
    55:"Fifty five",
}

print(d4)

'''
opt1:
("john" , 35, 100.89, 'residentatial', 'm' , ["python", "C++", "JAVA"]) :  "Some value",

opt2: error -3



'''

