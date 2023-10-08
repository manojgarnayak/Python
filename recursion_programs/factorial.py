# Program to find the factorial of a number

def manoj(n):
    if n == 6:
        return 1
    return n*manoj(n+1)
m = manoj(1)
print(m)