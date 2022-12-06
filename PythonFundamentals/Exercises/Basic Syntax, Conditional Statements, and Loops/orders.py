n_orders = int(input())
total = 0
for i in range(0, n_orders, +1):
    price_per_capsule = float(input())
    if price_per_capsule > 100 or price_per_capsule <= 0:
        continue
    days = int(input())
    if days <= 0 or days > 31:
        continue
    capsules_needed = int(input())
    if capsules_needed <= 0 or capsules_needed > 2000:
        continue
    else:
        price = (capsules_needed * days) * price_per_capsule
        print(f'The price for the coffee is: ${price:.2f}')
        total += price
print(f'Total: ${total:.2f}')