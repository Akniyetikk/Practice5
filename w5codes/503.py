import re
s = input()
pn = input()
match = re.findall(pn, s)
print(len(match))
