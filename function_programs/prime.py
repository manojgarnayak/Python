# Program to find a number is prime or not

def prime(num):
    c = 0
    a = 1
    while a <= num:
        if num % a == 0:
            c = c + 1
        a = a + 1
    if c == 2:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
    
prime(int(input("Enter a number: ")))