# Program to find prime numbers within a range

def manoj(n,i):
    if n == i:
        return True
    elif n % i == 0:
        return False
    else:
        return manoj(n,i+1)
    
m = int(input("Enter a range: "))
for x in range(2,m):
    if manoj(x,2):
        print(x,"is a prime number")
    else:
        print(x,"is not a prime number")