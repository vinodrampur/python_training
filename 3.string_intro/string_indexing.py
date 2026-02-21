sport='baseball'

print(sport[4])

sport1='baseball is a sport played in US'
print(sport1[8]) # space-1 --->' ' , i-1, error -1

'''
slicing
var[start index(default=0): stop index(-1): step value(default=1)]
'''

print(sport[2:5]) #seb

print(sport[2:5:2]) # sb


print(sport[2:7:2]) #sbl

print(sport[0:7:3]) #bel


print("====slicing using negative indexing======")
sport='baseball'

'''
var[start index(default=0): stop index(-1): step value(default=1)]
'''
print(sport[3]) # e
print(sport[-5]) # e

print(sport[-1:-8:-1]) # llabesa --- > [-1:-8:1]


str1='Ankit'
print(str1[::-1])

str1='ABBA'
str1="MalyalaM"
str1="MoM"

#var[start index(default=0): stop index(-1): step value(default=1)]
if str1[::] == str1[::-1]:
    print("ITs a palindrome string")
else:
    print("ITs NOT a palindrome string")


#-ve slicing and step value
str1='ThinkPython'
print(str1[-1:-6:-2]) #nhy