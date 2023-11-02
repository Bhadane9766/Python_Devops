
# this program for the split the string and collect specifinc value like need only ip address

x = "02nov2023 10.10.20.20 80  100.100.200.200 8080 weapp.com"
print("Given string is:- ", x)

y = x.split()

print("split string o/p: ", y)

print(" ### method-1 #####\n")

print(y[1], y[3])    # this one way

print(" ### another method-2 #####\n")

z = " ".join([y[1], y[3]])
print(z)
