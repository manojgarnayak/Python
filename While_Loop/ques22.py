# Check whether a number is palliprime or not

num = 11
snum = str(num)
revnum = int(str(num)[::-1])
a = 1

if num == revnum:
    c = 0
    while a <= num:
        if num % a == 0:
            c = c + 1
        a = a + 1

if c == 2:
    print("It is a palliprime")
else:
    print("It is not a palliprime number")