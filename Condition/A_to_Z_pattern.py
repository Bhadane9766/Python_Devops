#  $$$$$$$$$$$$$$$$$$$ print A pattern  $$$$$$$$$$$$$$$$$$$$$ ##

n = int(input("Enter the no of row :"))
m = round(n/2)-1


for i in range(n):
    for j in range(n):
        if ((j==0 or j==n-1)and i!=0) or ((i==0 or i==m) and (j>0 and j<n-1)):
            print("*", end='')
        else:
            print(" ", end='')

    print()





##  $$$$$$$$$$$$$$$$$$$$$ Print B pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##    

# n = int(input("Enter the no of row :"))
# m = (n//2)
# for i in range(n):
#     for j in range(n):
#         if ((j==0 or j==n-1) and i!=0 or i==m or i==n-1) or ((i==0 or i==m or i==n-1) and (j>0 and j<n-1)):
#             print("*", end='')
#         else:
#             print(" ", end='')

#     print() 



##  $$$$$$$$$$$$$$$$$$$$$ Print C pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##   


# n = int(input("Enter t=]
# he no of row :"))
# m = round(n/2)-1


# for i in range(n):
#     print(f"{i}\t" , end='')
#     for j in range(n):
#         if (j==0) or (i==0 or i==n-1):
#             print("*", end='')
#         else:
#             print(" ", end='')

#     print() 



##  $$$$$$$$$$$$$$$$$$$$$ Print D pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##   


# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):
    
#     for j in range(n):
#         if j==0 or (j==n-1 and (i!=0 and i!=n-1)) or (i==0 or i==n-1) and (j>0 and j<n-1):
#             print("*", end='')
#         else:
#             print(" ", end='')

#     print()     


##  $$$$$$$$$$$$$$$$$$$$$ Print E pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##   


# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):
    
#     for j in range(n):
#         if j==0 or ((i==0 or i==m or i==n-1) and j!=0):
#             print("*", end='')
#         else:
#             print(" ", end='')

#     print()


##  $$$$$$$$$$$$$$$$$$$$$ Print F pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##   


# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):
    
#     for j in range(n):
#         if j==0 or ((i==0 or i==m) and j!=0) :
#             print("*", end='')
#         else:
#             print(" ", end='')

#     print()  


##  $$$$$$$$$$$$$$$$$$$$$ Print G pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##   


# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):
    
#     for j in range(n):
#         if j==0 or (j==n-2 and (i!=1 and i!=2 and i!=2)) or (i==0 and (j>0 and j<n-2)) or (i==n-1 and (j>0 and j<=n-2)) or (i==m and j>2):
#             print("*", end='')
        

#         else:
#             print(" ", end='')

#     print()  


##  $$$$$$$$$$$$$$$$$$$$$ Print H pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##   


# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):
    
#     for j in range(n):
#         if j==0 or j==n-1 or (i==m and (j>0 or j>n)):
#             print("*", end='')
        

#         else:
#             print(" ", end='')

#     print()   


##  $$$$$$$$$$$$$$$$$$$$$ Print I pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):
    
#     for j in range(n):
#         if i==0  or j==m and (i!=0 or i!=n-1) or i==n-1:
#             print("*", end='')
        

#         else:
#             print(" ", end='')

#     print() 

##  $$$$$$$$$$$$$$$$$$$$$ Print J pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):
    
#     for j in range(n):
#         if i==0  or j==m and (i!=0 or i!=n-1) or i==n-1 and (j<m):
#             print("*", end='')
        

#         else:
#             print(" ", end='')

#     print()  



##  $$$$$$$$$$$$$$$$$$$$$ Print K pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = round(n/2)-1

# a=0
# b=n-1
# c=2
# d=m+1

# for i in range(n):
#     for j in range(n):
#         if j==0:
#             print("*", end='')
#         if (i==a and j==b) :

#              print("*", end='')
#              a=a+1
#              b=b-1
#         elif (j==c and i==d):
#              print("*", end='')
#              c+=1
#              d+=1      
        

#         else:
#             print(" ", end='')

#     print() 


# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):
    
#     for j in range(n):
#         if i==0  or j==m and (i!=0 or i!=n-1) or i==n-1:
#             print("*", end='')
        

#         else:
#             print(" ", end='')

#     print() 

##  $$$$$$$$$$$$$$$$$$$$$ Print L pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = round(n/2)-1


# for i in range(n):
    
#     for j in range(n):
#         if j==0  or (i==n-1 and j>0) :
#             print("*", end='')
        

#         else:
#             print(" ", end='')

#     print() 

##  $$$$$$$$$$$$$$$$$$$$$ Print M pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = (n//2)+1 
# a=0
# b=n-1

# for i in range(n):
    
#     for j in range(n):
#         if j==0 or j==n-1:
#             print("*", end='')
        

#         elif (i<m and (j==i or j== n-i-1)):
#             print("*", end='')


#         else:
#             print(" ", end='')

#     print() 

##  $$$$$$$$$$$$$$$$$$$$$ Print N pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = (n//2)+1 


# for i in range(n):
    
#     for j in range(n):
#         if j==0 or j==n-1:
#             print("*", end='')
        

#         elif (i==j):
#             print("*", end='')


#         else:
#             print(" ", end='')

#     print() 


# ##  $$$$$$$$$$$$$$$$$$$$$ Print O pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = (n//2)+1 


# for i in range(n):
    
#     for j in range(n):

#         if ((j==0 or j==n-1) and (i>0 and i<n-1)) or ((i==0 or i==n-1) and (j>0 and j<n-1)):
#             print("*", end='')
    

#         else:
#             print(" ", end='')

#     print() 


# ##  $$$$$$$$$$$$$$$$$$$$$ Print P pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = (n//2)+1 


# for i in range(n):
    
#     for j in range(n):

#         if j==0 or (j==n-1 and (i>0 and i<m-1)) or ((i==0 or i==m-1) and (j<n-1)):
#             print("*", end='')
    

#         else:
#             print(" ", end='')

#     print() 



##  $$$$$$$$$$$$$$$$$$$$$ Print Q pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = (n//2)+1 


# for i in range(n):
    
#     for j in range(n):
        
#         # below if condition for print O pattern 
#         if ((j==0 or j==n-2) and (i>0 and i<n-2)) or ((i==0 or i==n-2) and (j>0 and j<n-2)):
#             print("*", end='')
        
#         # below elif condition for print only tail of Q 
#         elif(i==n-1  and j==n-1):
#             print("*", end='')


#         else:
#             print(" ", end='')

#     print() 


# ##  $$$$$$$$$$$$$$$$$$$$$ Print R pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = (n//2)+1 


# for i in range(n):
    
#     for j in range(n):
        
         
#         if j==0 or (j==n-1 and (i!=0 and i!=m)) or ((i==0 or i==m) and j<n-1):
#             print("*", end='')
        
              
#         else:
#             print(" ", end='')

#     print() 

#  $$$$$$$$$$$$$$$$$$$$$ Print R pattern another another format $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = (n//2)-1 

# a=m+1
# b=3


# for i in range(n):
    
#     for j in range(n):
        
         
#         if j==0 or (j==n-1 and (i>0 and i<m)) or ((i==0 or i==m) and j<n-1):
#             print("*", end='')
        
#         elif (i==a and j==b):
#             print("*", end='')
#             a+=1
#             b+=1

                            
#         else:
#             print(" ", end='')

#     print() 
# # ##  $$$$$$$$$$$$$$$$$$$$$ Print S pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = (n//2)+1 


# for i in range(n):
    
#     for j in range(n):
        
         
#         if ((i==0 or i==m-1 or i==n-1) and (j!=0 and j!=n-1)) or (j==0 and i>0 and i<m) or (j==n-1 and i>=m and i<n-1):
#             print("*", end='')
        
              
#         else:
#             print(" ", end='')

#     print()

##  $$$$$$$$$$$$$$$$$$$$$ Print T pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = (n//2)


# for i in range(n):
    
#     for j in range(n):
        
         
#         if i==0 or j==m:
#             print("*", end='')
        
              
#         else:
#             print(" ", end='')

#     print() 


##  $$$$$$$$$$$$$$$$$$$$$ Print U pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = (n//2)+1 


# for i in range(n):
    
#     for j in range(n):
        
         
#         if ((j==0 or j==n-1) and i!=n-1) or (i==n-1 and (j!=0 and j!=n-1)):
#             print("*", end='')
        
              
#         else:
#             print(" ", end='')

#     print()

# ##  $$$$$$$$$$$$$$$$$$$$$ Print V pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# #n = int(input("Enter the no of row :"))
# #m = (n//2)+1 

# a=0
# b=7

# for i in range(4):
    
#     for j in range(7):
                 
#         if (i==j):
#             print("*", end='')

#         elif(i==a and j==b-1):

#             print("*", end='')

#             a=a+1
#             b=b-1
        
              
#         else:
#             print(" ", end='')

#     print()


##  $$$$$$$$$$$$$$$$$$$$$ Print W pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

#n = int(input("Enter the no of row :"))
#m = (n//2)+1 

# a=0
# b=3

# for i in range(4):
    
#     for j in range(7):
                 
#         if j==0 or j==6 or (i==2 and j==5) or (i==1 and j==4):
#             print("*", end='')
        
        

#         elif(i==a and j==b):

#             print("*", end='')
#             a=a+1
#             b=b-1

        
              
#         else:
#             print(" ", end='')

#     print()

# ##  $$$$$$$$$$$$$$$$$$$$$ Print X pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# #n = int(input("Enter the no of row :"))
# #m = (n//2)+1 

# a=0
# b=6

# for i in range(7):
    
#     for j in range(7):  

#         if(i==a and j==b):

#             print("*", end='')
#             a=a+1
#             b=b-1
#         elif (i==j):
#             print("*", end='')
        
              
#         else:
#             print(" ", end='')

#     print()

##  $$$$$$$$$$$$$$$$$$$$$ Print Y pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = (n//2)

# a=0
# b=n-1

# for i in range(n):
    
#     for j in range(n):  

#         if((i==j) and j<m) or j==m and i>m-1:

#             print("*", end='')
            
#         elif(i==a and j==b and i<=m):
#             print("*", end='')

#             a+=1
#             b-=1
        
        
              
#         else:
#             print(" ", end='')

#     print()


##  $$$$$$$$$$$$$$$$$$$$$ Print Z pattern $$$$$$$$$$$$$$$$$$$$$$$$$$$$ ##

# n = int(input("Enter the no of row :"))
# m = (n//2)

# a=1
# b=n-2

# for i in range(n):
    
#     for j in range(n):  

#         if(i==0 or i==n-1):

#             print("*", end='')
            
#         elif(i==a and j==b):
#             print("*", end='')

#             a+=1
#             b-=1
        
        
              
    #     else:
    #         print(" ", end='')

    # print()

