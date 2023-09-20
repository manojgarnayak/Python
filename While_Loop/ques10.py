# convert all the single characters in the list and add them

lst = ['1','2','3']
l = len(lst)-1
sum = 0
while l > 0:
    sum = sum + int(lst[l])
    l = l - 1

print(sum)