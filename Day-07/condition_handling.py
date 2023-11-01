
import sys

type = input("enter instance_type:")

if type == "t2.micro":
    print(" the pricing of the {type}  is 2$ per month")


elif type == "t2.medium":
    print(" the pricing of the {type}  is 4$ per month")


elif type == "t2.large":
    print(" the pricing of the {type} is 8$ per month")

else:
    print("##### Invalid input  #####")

