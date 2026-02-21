# conditions, jump the code, break, looping. for , while, if etc
# to check if the user can vote or not

#age = 21

age = int(input("Enter the age of the person: ")) # input function ALWAYS treats the input given as a string, for eg 21 will be saved as "21"
# age = int("21") --> age=21
#age=int(age) # "21" to 21 # type casting.

if age >= 18:# "21" > =18 - if we dont change input function so error  - # TypeError: '>=' not supported between instances of 'str' and 'int'
    print("You are allowed to vote")
    print("I am the second line here in the same if block")
    if age >20:
        print("Also greater than 20 as I am in the inner-if")
    else:
        print("I am of age between 18 and 20")

else:
    print("You are NOT allowed to vote")
    print("I am the second line here in the same else block")

#print("Print outside the if-else block and I will be exuected with both")