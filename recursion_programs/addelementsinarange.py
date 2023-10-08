# Program to add all the elements within a given range

def manoj(n):
    if n == 6:
        return 0
    return n+manoj(n+1)
m = manoj(1)
print(m)