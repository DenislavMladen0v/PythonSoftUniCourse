lines = int(input())
code = 0
result = 0
for i in range(lines):
    letter = input()
    code = ord(letter)
    result += code

print(f'The sum equals: {result}')

