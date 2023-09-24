# Count the number of the times a word is present in the string

strng = "we are what we are"
s = strng.split()
l = len(s)
a = 0
d ={}

while a < l:
    d[s[a]] = s.count(s[a])
    a = a + 1

print(d)