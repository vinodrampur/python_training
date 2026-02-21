'''
AVOID using while loop as much as possible. 
Its very easy to run into infinite loop problems with whole loop.
while loopps are "slightly better" than the for loops in terms of performance.
with while loop we can execute a set of statements "As long as the condition is true"

sytanx
while expression:
    <lines of code>

Use it ONLY and ONLY when you are VERY Sure of the exit criteria - exit of the loop
'''

count = 2
while count < 5:
    print(count) # 2,3,4
    count +=1 # count=count+1.... works for all operators for eg c*=1 c=c*1

print("========")
listx=[1,2,3,4,5,4,7,5,8,9,10]
# I want to print the values less than 5 from that list
listx.sort() # by default ascending order and for rever or descrneing order, gove sort(revers=True) 

i=0
while listx[i] < 5:
    print(listx[i])
    i+=1


i=1
while i < 6:
    print(i)
    if i == 3:
        break
    i+=1


