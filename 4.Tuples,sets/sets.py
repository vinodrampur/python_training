'''
Sets are another type of datatypes that are heterogenous and can contain a combination of other DT's as well, and sperated by a comma ','
sets can have numbers, strings, floats, etc so a combination of all other DT's under one variable called set_variable.
sets are iterables.
sets are "mutable" object, they are "unordered" and they DONOT allow duplicates.
Tuples can be defined as 2 types:
a. var = {}
b. set() internal set function

'''

listx=[] # empty list
tupx=() # empty tuple

print(listx)
print(tupx)
setx={}
print(setx) # empty dict
print(type(setx))
setx={1,2,3}
print(type(setx)) # <class 'set'>
setx=set() # empty set
print(type(setx))


setx={1,2,3,4,1,1,1,2,2,1}

print(setx) # {1, 2, 3, 4}


setx={1,2,'Think', "AI",4,5,6}
print(setx)

#print(setx[2]) # TypeError: 'set' object is not subscriptable

for i in setx:
    print(i)

set1= {1,2,3,4}
set2= {4,5,6,7}

print(set1.intersection(set2))
print(set1 & set2)

print(set1.union(set2))
print(set1 | set2)

print(set2.difference(set1))
print(set2-set1)

print("====mutability====")

set1={1,2,3,4}
set1.add(6)
print(set1)

print(set1.pop()) # LIFO - is not possible becoz unordered.

set1.remove(6)
print(set1)

newset=set1.copy()

print(hash(43))
print(hash("thinkPythonAI"))

print("=========Sets can be immutable- there is a special case in sets called frozensets=========")

set1={1,2,3,4}
set1.add(8)

fset=frozenset(set1)

print(fset) # frozenset({1, 2, 3, 4, 8})