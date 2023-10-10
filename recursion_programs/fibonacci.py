# Program to print the fibonacci series of nth term

def manoj(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return manoj(n-2) + manoj(n-1)

m = int(input("Enter the nth term: "))
for i in range(1,m):
    print(manoj(i))