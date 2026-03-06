import re
s = input()
upletters = re.findall(r'[A-Z]', s)
print(len(upletters))
