
from platform import java_ver
from traceback import print_tb


n = int(input("enter the number of row: "))  # take input from user

i = 1
while(n>0):
    b = 1
    while(b<i):
        print(" ", end=" ")
        b+=1
    j = 1
    while(j<=(n*2)-1):
        print("*", end=" ")
        j+=1

    print()    
    n=n-1
    i+=1
    