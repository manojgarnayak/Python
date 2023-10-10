# Program to add all the elements of a set

def manoj(l):
    if len(l) == 0:
        return 0
    return l.pop() + manoj(l)
s = {1,2,3,4,5}
m = manoj(s)
print(m)