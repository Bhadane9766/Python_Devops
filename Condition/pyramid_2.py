n = int(input("enter no of row: "))
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            print("*", end=" ")
        elif i==j:
            print("*", end=" ")    
        else:
            print(" ", end=" ")
    print()

    