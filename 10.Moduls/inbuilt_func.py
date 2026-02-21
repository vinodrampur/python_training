import math 

a=math.sqrt(4)
print(a)

print(math.pow(2,3))

print(math.factorial(5)) # 5*4*3*2*1

# pls explore more functions from math and os and sys modules.
# input() - always stores as string then we use type casting based on the input we need.
age=45.56
print(eval('age+15')) # to evaluate an expression that is defined as a string.

str1="think"
print(eval(" str1+ 'pythonAI' "))

""" x=eval(input("enter the value of x : "))
print(x)
print(type(x)) """

print("========f strings========")
milk_price=4.89
gas_price=4.56

print(gas_price)
# prior to 3.2 Py
# Placeholder - {} - based on the value of the varaible we had to provide a placeholder. for eg, {%f}gas_price, {%d}, {%c}, {%s}
# f- strings, f - format strings - you can use them anywhere you have strings, like in print(), in return f"This is a f-string return"
print(f'The gas price for today is {gas_price} and the milk price is {milk_price}, and the gas price yesterday was {gas_price-.5}')

