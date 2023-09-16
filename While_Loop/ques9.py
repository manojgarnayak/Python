# Program to prove it is a emirip number

num = 17
revnum = int(str(num)[::-1])
if num != revnum :
    c = 0
    a = 1
    while a <= num:
        if num % a == 0:
            c = c + 1
        a = a + 1
    if c == 2:
        d = 0
        b = 1
        while b <= revnum:
            if revnum % b == 0:
                d = d + 1
            b = b + 1
        if d == 2:
            print("emrip")
        else:
            print("not emirip")
    else:
        print("not emirip")
else:
    print("not emirip")   