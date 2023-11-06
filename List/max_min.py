a= []
x = int(input("enter the lenght of list: "))
for i in range(x):
    list = int(input("Enter the number: "))
    a.append(list)
print("element in the list : ", a)
print ("### result ####")
print("max number is :", max(a))
print("min number is :" , min(a))
