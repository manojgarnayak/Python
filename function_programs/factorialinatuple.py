# Find the factorial of all the elements present in the tuple

def factorial(tup):
    lst = []
    a = 0
    l = len(tup)
    fact = 1
    while a < l:
        fact = fact * tup[a]
        lst.append(fact)
        a = a + 1
    print(tuple(lst))

factorial(eval(input("Enter a tuple: ")))