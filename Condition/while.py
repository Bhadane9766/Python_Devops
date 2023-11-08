# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
# multiplication by 3 print >>>> Fizz
# multiplication by 5 print >>>> Buzz
# multiplication by 3 & 5 print >>>> FizzBuzz

# hint use for loop

from tkinter import E


print( "\t\t\t\t\t****Welcome to FizzBuzz program****")

for i in range(1,51):
    if ((i%3==0) and (i%5==0)):
        print("Fizz-Buzz")
    elif (i%5==0):
        print("Buzz")
    elif (i%3==0):
        print("Fizz")
    else:
        print(i)

