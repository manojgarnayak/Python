# Print the multiplication table of a number

def multable(num):
    a = 1
    while a < 11:
        print(num,"*",a,"=",num*a)
        a = a + 1

multable(int(input("Enter the number: ")))