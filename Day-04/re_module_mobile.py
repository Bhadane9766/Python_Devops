from ast import pattern
import re

def valid_mobile_number():

    while True:
        mobile_number = input(" Enter 10 digit mobile_number: ")
        pattern = r'^[0-9]\d{9}$'
        if re.match(pattern, mobile_number):
            return mobile_number
        else:
            print(f"{mobile_number}\tInvalid mobile number. Please enter valid 10 digit mobile number")



user_mobile_number = valid_mobile_number()
print("Entered mobile number is valid", user_mobile_number)
