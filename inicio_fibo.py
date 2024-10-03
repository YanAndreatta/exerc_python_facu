a = 0
b = 0
for i in range(10):
    if i == 1:
        a = i
    c = a + b
    a = b 
    b = c
    print(f"{c}", end=" ")