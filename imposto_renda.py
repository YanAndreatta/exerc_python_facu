value_1 = float(input())
taxa = 0

if value_1 > 1000.01:
    if value_1 < 2000:
        taxa += (value_1 - 1000) * 0.1
    else:
        taxa += 1000 * 0.1

if value_1 > 2000.01:
    if value_1 < 3000:
        taxa += (value_1 - 2000) * 0.2
    else:
        taxa += 1000 * 0.2

if value_1 > 3000.01:
    if value_1 < 4000:
        taxa += (value_1 - 3000) * 0.3
    else:
        taxa += 1000 * 0.3

if value_1 > 4000.01:
    if value_1 < 5000:
        taxa += (value_1 - 4000) * 0.4
    else:
        taxa += 1000 * 0.4

if value_1 > 5000:
    taxa += (value_1 - 5000) * 0.5

print(f"{taxa:.2f}")
