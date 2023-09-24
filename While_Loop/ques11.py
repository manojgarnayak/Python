# Program to find all the even numbers from the list

lst = [1,6,98,55,44,89]
l = len(lst)
emplst = []
a = 0
while a < l:
    if lst[a] % 2 == 0:
        emplst.append(lst[a])
    a = a + 1

print(emplst)

