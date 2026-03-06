import re
s = input()
pattern = input()
escapedpattern = re.escape(pattern)
matches = re.findall(escapedpattern, s)
print(len(matches))
