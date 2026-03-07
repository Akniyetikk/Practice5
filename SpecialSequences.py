#Special Sequences:
#\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
#\b	Returns a match where the specified characters are at the beginning or at the end of a word
#(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
#r"ain\b"	

#\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
#(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
#r"ain\B"	

#\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
#\D	Returns a match where the string DOES NOT contain digits	"\D"	
#\s	Returns a match where the string contains a white space character	"\s"	
#\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
#\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
#\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
#\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

ex1
import re
txt = "The rain in Spain"
#Check if the string starts with "The": 
#['The']
#Yes, there is a match!
x = re.findall("\AThe", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")

ex2
import re
txt = "The rain in Spain"
#Check if "ain" is present at the beginning of a WORD:
#[]
#No match
x = re.findall(r"\bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

ex3
import re
txt = "The rain in Spain"
#Check if "ain" is present at the end of a WORD:
#['ain', 'ain']
#Yes, there is at least one match!
x = re.findall(r"ain\b", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

ex4
import re
txt = "The rain in Spain"
#Check if "ain" is present, but NOT at the beginning of a word:
#['ain', 'ain']
#Yes, there is at least one match!
x = re.findall(r"\Bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

ex5
import re
txt = "The rain in Spain"
#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

ex6
import re
txt = "The rain in Spain"
#Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

ex7
import re
txt = "The rain in Spain"
#Return a match at every no-digit character:
x = re.findall("\D", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

ex8
import re
txt = "The rain in Spain"
#Return a match at every white-space character: [' ', ' ', ' ']
x = re.findall("\s", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

ex9
import re
txt = "The rain in Spain"
#Return a match at every NON white-space character:
x = re.findall("\S", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

ex10
import re
txt = "The rain in Spain"
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

ex11
import re
txt = "The rain in Spain"
#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

ex12
import re
txt = "The rain in Spain"
#Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
