# Program to find if the number is Emirip number or not

def emirip(n,i):
    if n == i:
        return True
    elif n % i == 0:
        return False
    else:
        return emirip(n,i+1)
    
num = int(input("Enter a number: "))
revnum = int(str(num)[::-1])
if num != revnum and emirip(num,2) and emirip(revnum,2):
    print(num, "It is a emirip number")
else:
    print(num, "It is not a emirip number")