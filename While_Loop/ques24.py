# Program to find the largest element in the list without using sort function

lst = [7,1,8,22,99,123]
l = len(lst)
max = lst[0]
a = 0
while a < l:
    if lst[a] > max:
        max = lst[a]
    a = a + 1

print(max)