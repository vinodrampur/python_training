'''
4 types of params/args:
a. Positional arguments or required arguments
b. Default args
c. Variable length args or vargs
d. Keyword length args or kwargs

'''

# positional
def add(x,y,z):
    print(x+y+z)

#add(2,3) # TypeError: add() missing 1 required positional argument: 'z'

add(1,2,3)

#default args - we provide a value during the function def.
# default args ALWAYS are after the positonal args
# this value is chosen if there is no value givem during the functon call
# but if there is a value that is given during the functon call, then that is considered and not the default value.

y=5
a=12
y=3

def add(x,z,y=5):
    print(x+y+z)

add(1,2,3) # error. z=5, y=3 (overitten)

#def add(x,y=5,z):
add(1,3) # 8....error...... # parameter without a default follows parameter with a default - default arg shud be AFTER the positional arg


# variable length arg - * stores internally as tuple

def feb_batch_students_names(*names): # ('Anand', 'Anisha', 'Butchi', 'Sudhkar', 'Nancy', 'Sapphire')
    print("The names of my feb batch students are: ",names)


feb_batch_students_names("Anand","Anisha","Butchi","Sudhkar","Nancy","Sapphire")

print("===========")
def area_of_cube(l,b=10,*h): # h=(2,6), h=(3,)
    area=l*b*h
    #print(l,b,h)
    print(area)

area_of_cube(12,14,2)
#area_of_cube(5,2,3) #(3, 3, 3, 3, 3, 3, 3, 3, 3, 3)

tupleeg=(2,4)
print(10*tupleeg) # (2,4,2,4)


'''
kwargs -> keyword length args - v v v v imp - for multiple reasons, this is int fav, code optimization.
keyword -> name = "ankit", x=5. in terms of python are keywords
** - kwargs
stored as dictionary (k1:v1,K2;v2.....)
'''


print("============kwargs========")

def students(**student_details):
    print(student_details)  # name:<name>, timezone: <EST>, coding_exp:True
    #{'name': 'Anand', 'timezone': 'IST'}

students(name="Anand", timezone="IST")



print("=================intq - all data params============")

def all_parms(name,*lang,country="USA",**books): # bookname1:author1
    print("All data about ", name)
    print(name, "lives in ", country, "and he has knowledge of ", lang, "and he enjoys these books from the resp authors: ", books)

all_parms("John","English","French","Python", "C++", book1="author1", book2="author2")




 