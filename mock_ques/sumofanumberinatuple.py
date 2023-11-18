# Program to find out sum of a number in a given tuple 
# input  example: (123,24,12,11)
# output example: [6,6,3,2]

def sumtup(ele):
    lst = []
    for i in ele:
        sum = 0
        for j in str(i):
            sum = sum + int(j)
        lst.append(sum)
    print(lst)

inp = eval(input("Enter a tuple of elements: "))
sumtup(inp)