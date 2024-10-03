a = int(input())
result = 0
for i in range(1,(a//2)+1):
    if a % i == 0:
        result += i
if result == a:
    print("sim")
else:
    print("não")