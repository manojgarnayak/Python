# Program to find the factorial of a number

def factorial(num):
    fact = 1
    a = 1
    while a <= num:
        fact = fact * a
        a = a + 1

    print(fact)

factorial(int(input("Enter a number: ")))