# Add all the even digits and multiply all the odd digits of a number

num = 123455432
snum = str(num)
l = len(snum)
a = 0
sum = 0
mul = 1
while a < l:
    if int(snum[a]) % 2 == 0:
        sum = sum + int(snum[a])
        a = a + 1
    else:
        mul = mul * int(snum[a])
        a = a + 1
print(sum)
print(mul)