# Find all the prime numbers within a list 

def primelst(lst):
    newlst = []
    l = len(lst)
    a = 0
    while a < l:
        c = 0
        num = 1
        while num <= lst[a]:
            if lst[a] % num == 0:
                c = c + 1
            num = num + 1
        if c == 2:
            newlst.append(lst[a])
        a = a + 1
    print(newlst)
    
primelst(eval(input("Enter a list: ")))