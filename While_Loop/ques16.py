# Program to print all the pallindromic numbers present in the list

lst = [11,34,66,89,67,99,88,56,44]
newlst = []
l = len(lst)
a = 0
revnum = 0
while a < l:
    revnum = int(str(lst[a])[::-1])
    if (revnum == lst[a]):
        newlst.append(revnum)
    a = a + 1

print(newlst)