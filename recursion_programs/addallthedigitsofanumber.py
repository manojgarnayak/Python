# Program add all the digits of a number

def manoj(num,n):
    if n == len(num):
        return 0
    return int(num[n]) + manoj(num,n+1)

m = manoj(str(521),0)
print(m)