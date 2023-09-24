# Program to prove whether a number is prime or not using break keyword

def prime(num):
    a = 2
    c = 0
    while a < num:
        if num % a == 0:
            c = c + 1
            break
        a = a + 1
    if c == 0:
        print(num, "It is a prime number")
    else:
        print(num,"It is not a prime number")

prime(int(input("Enter a number: ")))