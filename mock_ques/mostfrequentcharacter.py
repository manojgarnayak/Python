# Find the most frequent character in the string

s = "we are what we are"
d = {}
for i in s:
    d[i] = s.count(i)

maximum = max(d.values())
for a, b in d.items():
    if b == maximum:
        print(a)