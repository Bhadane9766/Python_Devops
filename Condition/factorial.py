
# #####################################################################

# import math

# n=int(input("enter the number: "))

# if(n<0):
#     print("factorial does not exist for negative numbers")
# elif(n==0):
#     print("factorial of 0 is 1")
# else:
#     print(f"The factoril of {n} is :", math.factorial(n))        


##############################################################################

# write a factorial program by using  loop

# n = int(input("Enter the number: "))
# fact = 1

# if(n<0):
#     print("factorial doe not exist for negstive number")

# elif(n==0):
#     print("factorial of 0 is 1")

# else:
#     for i in range (1,n+1):

#         fact = fact*i
#     print(f"The factorial of {n} is :",fact)


##############################################################

# write a program for factorial by using while 

n = int(input("Enter the number:"))
fact = 1

if(n<0):
    print("factorial does not exit for negative number")

elif(n==0):
    print("Factorial of 0 is 1")

else:
    while(n>0):
        fact=fact*n
        n-=1
    print("the factorial of {n} is:", fact)


   
