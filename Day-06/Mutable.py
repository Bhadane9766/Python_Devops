
def immdemo(mylist):
    mylist[0] = mylist[0] + 10
    print(" this is function output:", mylist)



list = [10,20,30,40,50]
print("output is outside list: ", list) 
immdemo(list)