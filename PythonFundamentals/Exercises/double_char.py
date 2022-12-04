cmd = input()  #Hello
result = ""
while cmd != "End":
    if cmd != "SoftUni":
        for i in cmd:
            result += i*2
        print(result)
    result = ""
    cmd = input()


