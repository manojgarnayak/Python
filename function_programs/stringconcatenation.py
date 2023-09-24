# Program to concatenate 2 strings and convert them to uppercase

def upper(first,last):
    full = first + "_" + last
    print(full.upper())

first = input("Enter your first name: ")
last = input("Enter your last name: ")

upper(first,last)