# Metro selection program
# if-elif - > if - elseif 

route= input("Enter the route you want to undertake: ")
#route.casefold()

if route == "sarjapur":
    print("Please take the yellow line")
elif route == "marathalli": # elseif
    print("Please take the red line ")
elif route == "hsr": # elseif
    print("Please take the orange line ")
elif route == "electronics city": # elseif
    print("Please take the blue line ")
elif route == "jayanagar": # elseif
    print("Please take the Grey line ")
else:
    print("Please check your selection ", route)
