value = int(input())
a = 0
b = 0

print(a, end="-")
if value != 1:
    for i in range(1,value):
        if i == 1:
            a = i
        c = a + b
        a = b
        b = c
        print(c, end="-")

