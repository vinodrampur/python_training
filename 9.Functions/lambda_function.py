'''
lambda --> unknown or anonymous or no name.
so no name is the biggest challenge when dealing with lambda -> becoz there is no name for the funciton.
how to call the func that has no name?
no def keyword 

syntax:
lambda parmeter_list:expression.
'''

#add two nos
#print(lambda x,y:x+y) #<function <lambda> at 0x10549b2e0>
a=lambda x,y,z:x+y+z
print(a(2,3,3))# print(5) - 5 # <lambda>() missing 1 required positional argument: 'z'

def add_two_nos(a,b,c):
    print(a+b+c)

add_two_nos(2,3,3)

area_of_cube=lambda l,b,*h:l*b*h
print(area_of_cube(4,3,3)) # 12*(3,)

#area_of_cube=lambda l,b,**h:l*b*h
#print(area_of_cube(4,3,a=2,c=3)) # 12*{a:2,c:3}
# how to fix this hpow to make some senses of it.


a=lambda x,y:x+y,x-y

print(a(3,1))