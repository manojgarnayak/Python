#s = "manoj kumar garnayak"
#print(s.index('a',14))

lst = [10,20,30,40]
l = len(lst)
newlst = [lst[0]]
sum = 0
a = 1

while a < l-1:
    sum = sum + lst[a]
    a = a + 1

newlst.append(sum)
newlst.append(lst[-1])

print(newlst)