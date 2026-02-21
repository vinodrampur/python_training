'''
its not a day 1 function - was not a part of orig py package
so we import it
reduce - you will use it where you want to reduce something from a big challenge to "one" single value.
more widely used in statistics like mean, mode etc.

'''
#P3: And then print  the sum of those elements.

from functools import reduce 

listx = [1,2,3,4,5,6,7,8,9,10]

print(sum(listx)) # 


n=0
for i in listx:
    n=n+i
print(n)


print("=====code optimized way with lambda and reduce======")

print(reduce(lambda x,y:x+y,listx))