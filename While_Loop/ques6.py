# Find all the prime numbers within a range from 1 to 30

num = 1
while (num <= 30):
    c = 0
    frstnum = 1
    while(frstnum <= num):
        if (num % frstnum == 0):
            c = c + 1
        frstnum = frstnum + 1
    if (c == 2):
        print(num)
    num =  num + 1