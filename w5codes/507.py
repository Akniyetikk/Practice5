import re
s = input()
pn = input()
rt = input()
result = re.sub(pn, rt, s)
print(result)
