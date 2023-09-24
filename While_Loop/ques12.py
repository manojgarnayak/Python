# Program to add all the even numbers and multiply all the odd numbers present in the list

lst = [1,3,6,7,9,5,8]
l = len(lst)
sum = 0
mul = 1
a = 0

while a < l:
    if lst[a] % 2 == 0:
        sum = sum + lst[a]
        a = a + 1
    else:
        mul = mul * lst[a]
        a = a + 1

print(sum)
print(mul)