'''
listx = [1,2,3,4,5,6,7,8,9,10]
Q1: Find the squares of the even numbers and show them in a list. 
FUQ: And then print  the sum of those elements.

Orig Q: Find the squares of the even numbers and show them in a list and then print the sum of that list of elements.
map,filter,reduce, with lambda - all in one line of code.

[4,16,36,64,100] -> sum of all these - should be the output
'''

#p1: Square of the nos in the list and show it as a new list

listx = [1,2,3,4,5,6,7,8,9,10]

print("First way ")
newlist=[] # empty list
for i in listx:
    i=i**2
    newlist.append(i)

print(newlist)

'''
map() - inbuilt function - but highly optimized
syntax - it needs a function and an iterable as two parameters.
'''

print("======Second way using map function only - much much better than the prev one=========")

def sq_values(n):
    return n**2

#print(map(sq_values,listx)) # <map object at 0x104e70eb0>

print(list(map(sq_values,listx)))
#print(list(res))

print("=======Best way using lambda and map together=========")

print(list(map(lambda n:n**2,listx)))