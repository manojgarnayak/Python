# Program to reverse a string

s = "manoj"
l = len(s)-1
emps = ""

while l >= 0:
    emps = emps + s[l]
    l = l - 1

print(emps)