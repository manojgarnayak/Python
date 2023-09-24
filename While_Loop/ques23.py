# Program to find all the prime numbers present in the list

lst = [2,5,6,7,4,9,11]
a = 0
l = len(lst)
while a < l:
    c = 0
    t = 1
    while t <= lst[a]:
        if lst[a] % t == 0:
            c = c + 1
        t = t + 1
    if c == 2:
        print(lst[a])
    a = a + 1