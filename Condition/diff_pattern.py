
# ## $$$$$$$$$$$$$$$$$  Increasing tringle $$$$$$$$$$$$$$$$$$$$


# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):
#     for j in range(i+1):
#             print("*", end='')

#     print()

''' OUTPUT
*
**
***
****
*****

'''

# ## $$$$$$$$$$$$$$$$$  Decreasing tringle $$$$$$$$$$$$$$$$$$$$

# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):
#     for j in range(i,n):
#             print("*", end='')

#     print()

''' OUTPUT
*****
****
***
**
*

'''

# ## $$$$$$$$$$$$$$$$$  Right tringle $$$$$$$$$$$$$$$$$$$$

# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):

#     for j in range(i,n):             # this loop for print blank space decreasing tng
#             print(" ", end='')

#     for j in range(i+1):             # loop for print * in increasing tringle
#             print("*", end='')

#     print()

''' OUTPUT
     *
    **
   ***
  ****
 *****

'''

## $$$$$$$$$$$$$$$$$  Left Right tringle $$$$$$$$$$$$$$$$$$$$


# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):

#     for j in range(i+1):             # this loop for print blank space increasing tng
#             print(" ", end='')

#     for j in range(i,n):             # loop for print * in decreasing tringle
#             print("*", end='')

#     print()

''' OUTPUT
 *****
  ****
   ***
    **
     *

'''

# $$$$$$$$$$$$$$$$$  Hill tringle $$$$$$$$$$$$$$$$$$$$


# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):


#     for j in range(i,n):             # loop for print "space" in decreasing tringle
#             print(" ", end='')
    

#     for j in range(i):             # this loop for print * increasing tng
#             print("*", end='')

#     for j in range(i+1):             # this loop for print * increasing tng
#             print("*", end='')  

#     print()

''' OUTPUT
     *
    ***
   *****
  *******
 *********
    
'''


# $$$$$$$$$$$$$$$$$  Reverse Hill tringle $$$$$$$$$$$$$$$$$$$$


# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):


#     for j in range(i+1):             # loop for print "space" in increasing tringle
#             print(" ", end='')
    

#     for j in range(i,n):             # this loop for print * decreasing tng
#             print("*", end='')

#     for j in range(i,n-1):             # this loop for print * decreasing tng
#             print("*", end='')  

#     print()

'''OUTPUT
 *********
  *******
   *****
    ***
     *
'''

# $$$$$$$$$$$$$$$$$  Diamond * pattern $$$$$$$$$$$$$$$$$$$$

# note : just added hill pattern + reverse hill patthern

# hill patthern code

n = int(input("Enter the no of row :"))
m = round(n/2)-1


for i in range(n-1):


    for j in range(i,n):             # loop for print "space" in decreasing tringle
            print(" ", end='')
    

    for j in range(i):             # this loop for print * increasing tng
            print("*", end='')

    for j in range(i+1):             # this loop for print * increasing tng
            print("*", end='')  

    print()

#  Reverse hill code

for i in range(n):


    for j in range(i+1):             # loop for print "space" in increasing tringle
            print(" ", end='')
    

    for j in range(i,n):             # this loop for print * decreasing tng
            print("*", end='')

    for j in range(i,n-1):             # this loop for print * decreasing tng
            print("*", end='')  

    print() 

    
''' OUTPUT
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *

'''
