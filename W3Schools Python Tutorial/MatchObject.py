ex1
import re
#The search() function returns a Match object: <_sre.SRE_Match object; span=(5, 7), match='ai'>
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match

ex2
import re
#Search for an upper case "S" character in the beginning of a word, and print its position: (12, 17)
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

ex3
import re
#The string property returns the search string: The rain in Spain
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

ex4
import re
#Search for an upper case "S" character in the beginning of a word, and print the word: Spain
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
