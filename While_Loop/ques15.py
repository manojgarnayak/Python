# Program to reverse all the elements of the list

lst = [11,23,76,89,53]
rlst = []
l = len(lst)
a = 0

while a < l:
    rlst.append(int(str(lst[a])[::-1]))
    a = a + 1
    
print(rlst)