# Prove a number is prime or not
num = 12
frstnum = 1
c = 0
while (num >= frstnum):
    if (num % frstnum == 0):
        c = c + 1
    frstnum = frstnum + 1
if(c == 2):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")