from tkinter import N


def get_employees_info():
    name = input("Enter emp name:- ")
    emp_id = int(input("Enter employee ID:- "))
    email_id = input("Enter your email_id:- ")
    department = input("Enter your dept name:-")
    return name, emp_id, email_id, department

# call the function and get the employee details
emp_name, emp_emp_id, emp_email_id, emp_department = get_employees_info()

# Display the employee details
print("######   employee details mention delow    #####")
print("Name of the employee is:", emp_name)
print("Emp ID of the employee is:", emp_emp_id)
print("email ID of the employee is:", emp_email_id)
print("Department of the employee is:", emp_department) 