a = int(input())
mod = 0 
for i in range(1,a+1):
    if a % i == 0:
        mod += 1
if a <= 1:
    print("não")
elif mod <= 2:
    print("sim")
else:
    print("não")