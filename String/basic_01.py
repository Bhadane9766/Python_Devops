
# name = "python"
# for i in name:
#     print(i)

# print(i,end="") 

##### concatenation operator #####

#print("every" + "day")

##### replication #####

#print("###"*3)

##### Membership operator ##### (in , not in )

# name = "python"
# print("p" in "python")
# print("o" in name)
# print("t" not in name)

### string slicing  ###

# a = "hello man"
# print("output: ",a[::1])
# print("output: ",a[::-1])   # print reverse string
# print("output: ",a[::])     # all string print
# print("output: ",a[0:5:-1])
# print("output: ",a[0:5:])
# print("output: ",a[3:-1])  # hello ma
# print(len(a))

#### string len() function ####

# from operator import le, rshift

### reverse string ########

# a = "python"
# for i in range(len(a)-1,-1,-1):
#     print(a[i], end="")

##### write program for count vowels and cons #####

# a = input("Enter string :- ")
# vowels=0  #set the values
# cons=0

# for i in range(0,len(a)):
#     if(a[i]!=" "):
#         if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U':
#             vowels= vowels + 1
#         else:
          
#             cons=cons+1
# print(f"total number of vowels in given strings out of string lenght {len(a)} :-", vowels )
# print(f"total number of cons in given strings out of string lenght {len(a)} :-", cons )



####### write a program for calculate a letter in the given string ####

# y = input("Enter string:-")
# count=0

# for i in range(0,len(y)):
#     if(y[i]=='a'):
#         count= count+1
#     else:
#         pass

        
# print("toal a char is", count)  

##### write a program for count char from given string  #######  
s = input("enter string:-")

c = s.count("a") +s.count("s")
print(c)
