#P2: Find the even nos and show them in a list/tuple
# filter() - another inbuilt function - similar syntax - first param is functon and second is an iterable.
# filters based on the condition - thats it.

listx= [1,2,3,4,5,6,7,8,9,10]

print("======first way=======")
newlist= []
for i in listx:
    if (i%2==0):
        newlist.append(i)
    
print(newlist)

print("======Better way with filter function=========")

def even_num(n):
    if (n%2==0):
        return n

#print(filter(even_num,listx)) # <filter object at 0x103944f70>
print(list(filter(even_num,listx)))


'''
map vs filter
map () is used when you have to work on "ALL" the data 
filter() - is used when you have to filter or select based on a criteria and hence you will be working with some of the members.
'''

print("======Final way with lambda and filter()=========")
print(list(filter(lambda n: n%2==0,listx)))