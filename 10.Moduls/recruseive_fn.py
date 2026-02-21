'''
recursion - is v tricky and thats why int fav.
A recursion function is a function where the function calls itself from within itself.
its easy to get into looping and hence you should ALWAYS think first about the EXIT criteria.
best eg is factorial for eg 5! = 5*4*3*2*1
another variant for the int q is eg 5 = 5+4+3+2+1
'''
import os 


def recursion_func(k):
    # think about the exit criteria i.e 1
    if k > 0:
        res = k * recursion_func(k-1)
    else: # whnever k=0 return 1
        res = 1
    return res

print("recursion")
#res=recursion_func(3)
k=eval(input("Enter the number that you want the factorial of: "))
res=recursion_func(k)
print(res)


print("Current dir is :")
print(os.getcwd())
os.chdir('..')
print("Current dir is :")
print(os.getcwd())

