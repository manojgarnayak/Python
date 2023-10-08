# Program to add the numbers present in a string

def manoj (s,n):
    if n == len(s):
        return 0
    return int(s[n]) + manoj(s,n+1)

m = manoj("1234",0)
print(m)