'''
listx=[1,2,3,4]
str1="ankit"
a for/while loop is used for iterating over a sequence. Sequence can be any DT which has a list of elements seperated by either comma or a string.
syntax:
for iterationVariable in Sequence/map:
    <lines of code inside the for loop>

'''

listx=[1,2,3,4]
# print all the elemtns of the listx one-by-one
for i in listx:
    print(i)
print("I am the next statement")


fruits = ("Oranges","bananas","apples","cherries")
for fruit in fruits:
    print(fruit)
    if fruit == "bananas":
        break

print("=======break========")
cars= ["Audi","Merc","RR", "BMW", "Hyundai", "RR", "Toyota"]

for car in cars:
    print(car)
    if car == "RR":
        break
    
print("=======continue========")
'''
continue - we just go (skip) the "current" iteration inside the loop - AND Continue to the next iteration.

'''

fruits = ("Oranges","bananas","apples","cherries")
for fruit in fruits:
   
    if fruit == "bananas":
        continue 
    print(fruit)

# range(start(0),stop(-1), step (default-1) - generate integers
# eg range(6) - 0,1,2,3,4,5
for x in range(6):
    print(x)
else:
    print("Will I get ever executed or not?")


'''
pass - is called a developers tool , to avoid syntactical errors. your final working code will "NEVER" have a pass statememnt.

'''

a=40
b=200

if a > b:
    pass 
else:
    print("This is the else part")


for num in (5,):
    print(num) # error......only 5......

for char in "Python":
    if char !='o':
        print(char) # Pyth.....
        #continue
    else:
        break
