lines = int(input())
result = 0

for i in range(lines):
    liters_water = int(input())
    result += liters_water
    if result > 255:
        result -= liters_water
        print("Insufficient capacity!")
print(result)
