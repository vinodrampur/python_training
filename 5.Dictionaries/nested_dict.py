family1 = {
    "child1":{
        "name":"Emily",
        "age": 20,
    },
    "child2": {
        "name": "John",
        "age":25,
    }
}

print(family1)
print(family1.keys())

print("======")

child1 = {
        "name":"Emily",
        "age": 20,
    }

child2= {
        "name": "John",
        "age":25,
    }

family2= {
    "child1": child1,
    "child2": child2,
}

print(family2)

print(family1['child2']['age']) # 25
print(family2['child2']['age']) # 25

# becoz internally both are going to be implemented in the first famly1 way.

'''
{
        "name": "John",
        "age":25,
    }
["age"]
'''

#listy=[(1,),(2,),(3,)]
listy=[(1,None),(2,None),(3,None)]
new2=dict(listy)
print(new2)
# error

listx=[1,2,3,4]
#print(listx.append(8))
print(listx)


