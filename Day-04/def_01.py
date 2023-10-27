num1= int(input("Enter first number:"))
num2= int(input("Enter second number:"))

def addition(num1, num2):
    add = num1 + num2
    return add

def multiplication(num1, num2):
    mul = num1 * num2
    return mul


def square(num1, num2):
    sq = num1**2 + num2**2
    return sq

print("addition:-", addition(num1, num2))
print("Multi:-", multiplication(num1, num2))
print("square addition:-", square(num1, num2))

print("###########################################################################")
add_result = addition(num1, num2)
mul_result = multiplication(num1, num2)
sq_result = square(num1, num2)

# Displaying results
print("Addition:", add_result)
print("Multiplication:", mul_result)
print("Sum of squares:", sq_result)




