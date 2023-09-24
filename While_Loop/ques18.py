# Prove a number is harshad number or not

num = 81
snum = str(num)
sum = 0
l = len(snum)
a = 0

while a < l:
    sum = sum + int(snum[a])
    a = a + 1

if num % sum == 0:
    print("It is a harshad number")
else:
    print("It is not a harshad number")