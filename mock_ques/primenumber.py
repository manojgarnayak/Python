#Program to find prime number within a given range using while loop and functions

def prime(start,end):
    while(start <= end):
        c = 0
        a = 1
        while(a <= start):
            if (start % a == 0):
                c = c + 1
            a = a + 1
        if (c == 2):
            print(start)
        start = start + 1

startnum = int(input("Enter the start number: "))
endnum = int(input("Enter the end number: "))
prime(startnum,endnum)