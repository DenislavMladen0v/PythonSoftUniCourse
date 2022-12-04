events = input()
coffee_count = 0
while events != "END":
    check = events.lower()
    if check == "cat" or check == "dog" or check == "movie" or check == "coding":
        if events.isupper():
            coffee_count += 2
        else:
            coffee_count += 1
    events = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)


