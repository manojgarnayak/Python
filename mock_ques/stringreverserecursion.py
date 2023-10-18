# Reverse a string using recursion

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

strng = eval(input("Enter a string: "))
spt = strng.split()
newstr = ""
for i in spt:
    rev = reverse(i)
    newstr = newstr + " " + rev

print(newstr)