# Program to find the prime program using return keyword

def prime(n):
    c = 0
    for i in range(2,n):
        if n % i == 0:
            c = c + 1
            break
    if c == 0:
        return True
    else:
        return False
    
num = int(input("Enter a number: "))

if prime(num):
    print(num,"It is a prime number")
else:
    print(num,"It is not a prime number")