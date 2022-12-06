str1 = input()
str2 = input()
lstr = ""
rstr = ""
lplusr = ""
last_string = str1
for i in range(len(str1)):
    lstr = str2[:i:]
    rstr = str1[i::]
    lplusr = lstr + rstr
    if last_string == lplusr:
        continue
    last_string = lplusr
    print(lplusr)
