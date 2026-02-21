sport = 'Basketball'

print(sport[4])


sport1 = "Basketball is a sport played in USA"
print(sport1[10]) #  " " .....error....  space is the right answer

'''
Slicing - 
var[start index(default = 0): stop index(-1): step value(default =1)]

'''

sport = 'Basketball'
print(sport[2:5]) # ske 

print(len(sport))
print(sport[1:8]) # ab.....asketba....asketb......

#print(sport[10]) # l....error
print(sport[1:12]) # error...... so 12 here is assumed as end of string.(data type)

print(sport[1:10:2]) # aktal
print(sport[1:10:3]) # aea


print(sport[:10]) # B-l - internally it is treated as [0:10:1]

print(sport[::]) # error...[0:10:1]... we get the whole string

#print(sport[1:10:0]) # error

print(sport[1:10:12]) # error.....a.....a-l..... a <space>