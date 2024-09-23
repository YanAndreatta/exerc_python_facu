value_1 = int(input())
value_2 = int(input())
value_3 = int(input())

if not (value_1 + value_2 > value_3 and value_1 + value_3 > value_2
        and value_2 + value_3 > value_1):
    print("inválido")
elif value_1 == value_2 and value_2 == value_3:
    print("equilátero")
elif value_1 == value_2 or value_2 == value_3 or value_1 == value_3:
    print("isósceles")
else:
    print("escaleno")
