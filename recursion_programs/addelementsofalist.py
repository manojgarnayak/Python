# Program to add all the elements of a list

def manoj(l,n):
    if n == len(l):
        return 0
    return l[n] + manoj(l,n+1)
m = manoj([10,20,30],0)
print(m)