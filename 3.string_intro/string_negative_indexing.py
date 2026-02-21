'''
Negative Slicing - Int fav
var[start index(default = 0): stop index(-1): step value(default =1)]
step value decides the direction of the move whether +ve or -ve

also how to reverse the string.
'''

name="Sudhakar"

print(name[3]) #h
print(name[-5])

print(name[-1:-9:-1]) # [-1:-9] ---> treated as [-1:-9:1].......name[-1:-12:-1] also same as the positvie side, go to the begining of the string basically.(based on total len)

print(name[-6:-2]) #dhak

print(name[::]) # Sudhakar
print(name[::-1]) # rakahduS 
# Palindrome string
'''
MoM

'''

name="MoM"
#name="MalyalaM"
#name="ABBA"
if name[::] == name[::-1]:
    print("Its a palindrome")
else:
    print("Its NOT a palindrome")


str1= "ThinkPythonAI"
print(str1[-1:-6:-2]) # r.....in.......space....IAnoht.....ra dh