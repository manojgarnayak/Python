# Add all the digits of a num 

num = 12345
snum = str(num)
l = len(snum) - 1
frstnum = 0
sum = 0
while (l >= frstnum):
    sum = sum + int(snum[l])
    l = l - 1
print(sum)