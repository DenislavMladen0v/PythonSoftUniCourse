lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
helmet_count = 0
sword_count = 0
shield_count = 0
shield_breaks = 0
armor_count = 0

for i in range(1, lost_fights+1):
    if i % 2 == 0:
        helmet_count += 1
    if i % 3 == 0:
        sword_count += 1
        if i % 2 == 0:
            shield_count += 1
            shield_breaks += 1
            if shield_breaks == 2:
                armor_count += 1
                shield_breaks = 0

total_expenses = (helmet_count * helmet_price) + (sword_count * sword_price) + (shield_count * shield_price) + \
        (armor_count * armor_price)

print(f"Gladiator expenses: {total_expenses:.2f} aureus")

