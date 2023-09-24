# Print out the pallindromic word present in a sentence

strng =  "your range is out of my radar"
s = strng.split()
l = len(s)
a = 0

while a < l:
    if s[a] == s[a][::-1]:
        print(s[a])
    a = a + 1