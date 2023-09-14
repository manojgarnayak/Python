# Prove a number is disarm number or not

num = 135
snum = str(num)
l = len(snum)
frstnum = 0
pow = 1 
disarm = 0
while (frstnum < l):
    disarm = disarm + int(snum[frstnum])**pow
    frstnum = frstnum + 1
    pow = pow + 1
if (disarm == num):
    print(num , "is a disarm number")
else:
    print(num ,"is not a disarm number")