# Program to find the number is palliprime or not

def palli(n):
    revnum = int(str(n)[::-1])
    if revnum == n:
        return True
    else:
        return False
    
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
if palli(num) and prime(num):
    print(num, "is a palliprime number")
else:
    print(num, "is not a palliprime number")