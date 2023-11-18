# Program to find words which are greater than given length n from an string
# input example : we are what we are
# size example : 3
# output example : are what are

def greatstr(inpstr,s):
    newstr = ""
    splt = inpstr.split()
    for i in splt:
        if len(i) >= s:
            newstr = newstr + " " + i
        
    print(newstr)

strinput = eval(input("Enter the string: "))
size = int(input("Enter the size: "))
greatstr(strinput,size)