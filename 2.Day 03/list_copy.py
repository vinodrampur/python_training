# diff between shallow copy and deep copy
listx = [1,2,3,4]
listy = listx # 
listz = listx.copy() #  copies the listx into listz


print("All the lists before any changes")
print(listx) # [1, 2, 3, 4]
print(listy) # [1, 2, 3, 4]
print(listz) # [1, 2, 3, 4]

print("All the lists after a change")
listx.append(8)

print(listx) #  [1, 2, 3, 4, 8]
print(listy) #  [1, 2, 3, 4, 8].....[1, 2, 3, 4]......[1, 2, 3, 4].......
print(listz) #  [1, 2, 3, 4, 8].....[1, 2, 3, 4]......[1, 2, 3, 4,8].........

