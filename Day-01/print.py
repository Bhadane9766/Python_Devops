# myfile = open('python.txt', 'w')
# print("welcome in python !!!", file = myfile)
# myfile.close()


##############z use return in the fuction ##########

# def fun1(x):
#     return x+1

# def fun2(a,b):
#     c = a+b
#     return c

# y=fun2(2,9)
# z=fun1(y)
# print("fun1 output is :-",z)
# print("fun2 output is :", y)   
# 
# 


##### Recursion menas function call itself.

def example():
    print("calling function itself within a function")

    example()

example()


