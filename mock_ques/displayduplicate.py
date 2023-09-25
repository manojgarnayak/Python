# Display all the duplicate value present in it in form of list

def duplicate(n):
    lst = []
    duplst = []
    for i in n:
        if i not in lst:
            lst.append(i)
        else:
            duplst.append(i)

    print("This is duplicate list",duplst)


duplicate([10,20,13.33,1+9j,10,13.33,True,"abcd",1+9j])