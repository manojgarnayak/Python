# Program to find the least frequent character in the list

s = "we are what we are"
d = {}
for i in s:
    d[i] = s.count(i)
minimum = min(d.values())
for a , b in d.items():
    if b == minimum:
        print(a)