price=1499.99
year=2026

fobj = open("File_handling/cost.txt","w+")
#fobj.write("Cost of the new iphone is $",price, "and the year of production is ,",year). write can only take one single argument.
#TypeError: TextIOWrapper.write() takes exactly one argument (4 given)
fobj.write("Cost of the new iphone is : $" + str(price) + " and the year of production is " + str(year))
fobj.seek(0)
res=fobj.read()
print(res)



