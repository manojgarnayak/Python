# Program to enter elements and add them to a list

def lst(lenght):
    newlst = []
    a = 0
    while a < lenght:
        ele = eval(input("Enter the element: "))
        newlst.append(ele)
        a = a + 1
    print(newlst)

lst(int(input("Enter the lenght of the list: ")))