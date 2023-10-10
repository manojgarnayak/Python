# Program to find if the number is prime or not

def manoj(n,i):
    if n == i:
        return True
    elif n % i == 0:
        return False
    else:
        return manoj(n,i+1)
    
m = int(input("Enter a number: "))
if manoj(m,2):
    print(m, "is a prime number")
else:
    print(m, "is not a prime number")