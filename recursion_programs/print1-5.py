#Program to print 1-5 using recursion

def manoj(n):
    if n == 6:
        return
    print(n)
    return manoj(n+1)
manoj(1)