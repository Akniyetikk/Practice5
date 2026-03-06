import re
s = input()
ss = input()
if re.search(ss, s):
    print("Yes")
else:
    print("No")
