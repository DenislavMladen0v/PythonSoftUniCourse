quantity = int(input())
days = int(input())
total = 0
spirit = 0


for i in range(1, days+1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total += quantity * 2
        spirit += 5
    if i % 3 == 0:
        total += quantity * (5 + 3)
        spirit += 13
    if i % 5 == 0:
        total += quantity * 15
        spirit += 17
        if i % 3 == 0:
            spirit += 30
    if i % 10 == 0:
        spirit -= 20
        total += 23
if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {total}")
print(f"Total spirit: {spirit}")


