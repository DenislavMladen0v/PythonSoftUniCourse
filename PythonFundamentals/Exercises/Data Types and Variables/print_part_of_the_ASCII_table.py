first_char = int(input())
second_char = int(input())
result = ""

for i in range(first_char, second_char+1):
    result += chr(i) + " "

print(result)