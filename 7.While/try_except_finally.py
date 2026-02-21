'''
Finally is optional- will have block of code that will get executed no matter what. this means whether exeception or not, finally will always work.

'''

r1=10
r2=5
#a=5

try:
    print(a)

except NameError as e:
    print("exception,",e)

finally:
    print("I am the finally block")

print("I am the statement after finally ")

'''
DB connections:
Step 1 : open conn to DB/File
step 2: Add/modify/delete operations
step 3: close the conn to db/File -------> v vv v v v vimp the most critical step. - this goes in finally.

'''

try:
    print("in try block")
    #print(a)
except:
    print("in except")
else: # else will excecute when there is no exception.
    print("in else")
finally:
    print("in finally")


#error.....in try, infinally..... also else.
try:
    print("in try block")
except:
    print("in except")

# try-except block is done here.

if 20 >30:
    print("True")
else: # else will excecute when there is no exception.
    print("False")

# error....in try, true...
