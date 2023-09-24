# Prove a number is xylem number or not

num = 12348 
snum = str(num)
l = len(snum)
a = 0
sum1 = 0
sum2 = 0

sum1 = int(snum[a]) + int(snum[l-1])
a = a + 1
while a < l-1:
    sum2 = sum2 + int(snum[a])
    a = a + 1

if sum1 == sum2:
    print("It is a xylem number")
else:
    print("It is not a xylem number")