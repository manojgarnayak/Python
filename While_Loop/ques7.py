# Prove a number is armstrong no or not

num = 153
snum = str(num)
l = len(snum)
arm = 0
frstnum = 0
while (frstnum < l):
    arm = arm + int(snum[frstnum])**l
    frstnum = frstnum + 1
if (arm == num):
    print(num , "is a armstrong number")
else:
    print(num, "is not a armstrong number")