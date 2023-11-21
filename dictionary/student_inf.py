### program for student info and print the output

student_DB={}     # create empty dictionary

# take input from user

while True:

    line=input("enter the id and name seperated by comma or press q to exit:")


    if line=='q':
        break
    id,name = line.split(',')
    student_DB.update({id:name})

# print the info

for x,y in student_DB.items():
    print(x,y)

# find key 

key= input("enter id of the student:")

if key in student_DB:
    print("ID is=", id, "value is=", student_DB([key]))

else:
    print("Given id is not found")    