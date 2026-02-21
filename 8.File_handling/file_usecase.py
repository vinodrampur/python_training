import os 

try:
    fobj=open("File_handling/log.txt","w+")
    #make sure the file exists and is writable 
    if fobj.writable: # boolean
        fobj.writelines("this is the first line of error in the log file \n followed by the seocnd error line \n and a third line of logs and error \n this is the fourth line ")
    if fobj.readable: # boolean
        fobj.seek(0)
        res=fobj.readlines() # returns list when there are multiple lines in the log file.
        #['this is the first line of error in the log file \n', ' followed by the seocnd error line \n', ' and a third line of logs and error \n', ' this is the fourth line ']
        print(res)
        counter=0
        for word in res:
            #if word == "error": # do not use this - hear the video again if yuo are confused
            if "error" in word: # if error exists inside word or not.
                print("Match found")
                counter+=1
            else:
                print("No Match found in the logs for error")



except Exception as msg:
    print("error - ",msg)

finally:
    file_len = os.path.getsize("File_handling/log.txt")
    print(file_len)
    print("no of times error happened today is :" , counter)
    if fobj.closed == False:
        print("the file is still open, lets close it")
        fobj.close() # ---this is the most important steps.
        print("the file is closed")
        print(fobj.closed)


