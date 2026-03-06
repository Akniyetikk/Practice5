import re
s = input()
def doubledigit(match):
    return match.group() * 2
result = re.sub(r'\d', doubledigit, s)
print(result)
