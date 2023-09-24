# Program to reverse the even characters in the string

strng = "Something is better than nothing and nothing is better than everything"
spt = strng.split()
l = len(spt)
a = 1
lst = []
lst.append(spt[0])
while a < l:
    if a % 2 == 0:
        lst.append(spt[a][::-1])
        a = a + 1
    else:
        lst.append(spt[a])
        a = a + 1
    
news = ""
ln = len(lst)
b = 0 
while b < ln:
    news = news + " " + lst[b]
    b = b + 1

print(news)