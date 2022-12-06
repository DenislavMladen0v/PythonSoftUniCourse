budget = float(input())
one_kg_flour = float(input())
eggs_price = one_kg_flour * 0.75
milk_price = (one_kg_flour + (one_kg_flour*0.25))/4
total_bread = 0
price_for_bread = one_kg_flour + eggs_price + milk_price
budget_remaining = budget

eggs_count = 0
current_bread_count = 0


while budget_remaining > 0:
    if budget_remaining > price_for_bread:
        total_bread += 1
        budget_remaining -= price_for_bread
        current_bread_count += 1
        eggs_count += 3
        if current_bread_count == 3:
            eggs_count -= total_bread - 2
            current_bread_count = 0
    else:
        break
print(f"You made {total_bread} loaves of Easter bread! Now you have {eggs_count} eggs and {budget_remaining:.2f}BGN left.")

