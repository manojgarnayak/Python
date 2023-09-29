# Prove a number is emirip number or not

def emirip(n):
    c = 0 
    for i in range(2,n):
        if n % 2 == 0:
            c = c + 1
            break

    if c == 0:
        return True
    else:
        return False
    
num = int(input("Enter a number:"))
revnum = int(str(num)[::-1])
if (revnum != num) and emirip(num) and emirip(revnum):
    print(num ,"is a emirip number")
else:
    print(num, "is not a emirip number")