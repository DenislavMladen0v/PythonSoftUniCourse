n = int(input())
negative_numbers = 0
negative = []
positive_numbers = 0
positive = []



for i in range(n):
    number = int(input())
    if number < 0:
        negative_numbers += number
        negative.append(number)
    else:
        positive_numbers += 1
        positive.append(number)

print(positive)
print(negative)
print(f"Count of positives: {positive_numbers}")
print(f"Sum of negatives: {negative_numbers}")