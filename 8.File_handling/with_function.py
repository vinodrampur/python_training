# with - will automatically close the fileobj - at the EOF. end of file.
# you will always use the with in working env - but we learnt the prev egs without with for the interviewers

with open("File_handling/temp_using_with.txt","w+") as fobj: # the whole code goes insise this with block
    try:
        fobj.writelines("This is the feb batch \n for professionals and has 16 students")
        fobj.seek(0)
        cont=fobj.readlines()
        print(cont)

    except Exception as msg:
        print(msg)

    finally:
        #print(fobj.closed) # False
        print("I am after finally")

print(fobj.closed) # True - no explicit fobj.close is required when using the "with" keyword