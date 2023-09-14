# Add all the elements present in the list

lst = [10,30,50,60,40]
sum = 0
frstnum = 0
l = len(lst)-1
while (l >= frstnum):
    sum = sum + lst[l]
    l = l - 1
print(sum)