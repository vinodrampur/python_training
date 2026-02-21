#open("firstfile.txt")  # FileNotFoundError: [Errno 2] No such file or directory: 'firstfile.txt' - so by default it takes the read mode.

# connection to the file
fobj=open("File_handling/Firstfile.txt","w+")
fobj.write("This is a test line, this is Feb batch for ThinkPythonAI professionals")

# read the contents of the file thru the same connection
fobj.seek(5) # index in the log file.
content=fobj.read()
print(content)

print(fobj.closed)
fobj.close() # explicitiy make sure you do not forget to do this - esp in in the ineterview. v v  imp
print(fobj.closed)
