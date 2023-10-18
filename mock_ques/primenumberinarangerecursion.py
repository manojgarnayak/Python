# Program to find Prime numbers within a range using recursion

def rec(n,i):
    if n == i:
        return True
    elif n % i == 0:
        return False
    else:
        return rec(n,i+1)
    
for j in range(20,51):
    if rec(j,2):
        print(j, "is a prime number")