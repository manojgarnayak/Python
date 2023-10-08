# Program to print 10-1 using recursion

def manoj(n):
    if n == 0:
        return
    print(n)
    return manoj(n-1)
manoj(10)