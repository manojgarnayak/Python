#Proof a number is a happy number or not

num = 125
snum = str(num)
l = len(snum)
sum = 0
mul = 1
a = 0

while a < l:
    sum = sum + int(snum[a])
    mul = mul * int(snum[a])
    a = a + 1

if sum == mul:
    print("It is a happy number")
else:
    print("It is not a happy number")