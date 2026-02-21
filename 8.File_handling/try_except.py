'''
Exception ---> Error handling
to handle edge cases predominantly

try,except,finally,raise,else
'''

# r1=int(input("enter the first number: "))
# r2=int(input("enter the second number: "))

# print(r1/r2) # ZeroDivisionError: division by zero

#print("important lines of code following the above that you want to execute")

r1=int(input("enter the first number: "))
r2=int(input("enter the second number: "))

# try:
#     print(r1/r2) 
#     print(a) # NameError: name 'a' is not defined

# except (ZeroDivisionError,NameError,ArithmeticError,IndentationError): # tuple
#     print("Got an error, please try again")

# except NameError:
#     print("Got an error, may be the variable is not defined.")


try:
    print(r1/r2)
    print(a)

# except Exception :
#     print("Error")

except ZeroDivisionError as msg : # as is alias, msg takes the string part of the error.
     print("Got an error, ",  msg)

except NameError as msg :
     print("Got an error, ",  msg)

except Exception as msg:
    print(msg)

print("important lines of code following the above that you want to execute")


