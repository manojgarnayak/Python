# Program to add all the elements of an list except its first and last element and present it in form of a list in which addition of all the middle elements are kept in between first and last element 
# input example: [10,20,30,40,50]
# output example: [10,90,50]

def addele(ele):
    sum = 0
    newlst = [ele[0]]
    l = len(ele)
    for i in range(1,l-1):
        sum = sum + ele[i]
    newlst.append(sum)
    newlst.append(ele[-1])
    print(newlst)

inp = eval(input("Enter a list of elements: "))
addele(inp)