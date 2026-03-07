#Metacharacters:
#[]	A set of characters	"[a-m]"	
#\	Signals a special sequence (can also be used to escape special characters)	"\d"	
#.	Any character (except newline character)	"he..o"	
#^	Starts with	"^hello"	
#$	Ends with	"planet$"	
#*	Zero or more occurrences	"he.*o"	
#+	One or more occurrences	"he.+o"	
#?	Zero or one occurrences	"he.?o"	
#{}	Exactly the specified number of occurrences	"he.{2}o"	
#|	Either or	"falls|stays"	
#()	Capture and group	 

ex1
import re
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m": ['h', 'e', 'a', 'i', 'i', 'a', 'i']
x = re.findall("[a-m]", txt)
print(x)

ex2
import re
txt = "That will be 59 dollars"
#Find all digit characters: ['5', '9']
x = re.findall("\d", txt)
print(x)

ex3
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o": ['hello']
x = re.findall("he..o", txt)
print(x)

ex4
import re
txt = "hello planet"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

ex5
import re
txt = "hello planet"
#Check if the string ends with 'planet':
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

ex6
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o": ['hello']
x = re.findall("he.*o", txt)
print(x)

ex7
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o": ['hello']
x = re.findall("he.+o", txt)
print(x)

ex8
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o": []
x = re.findall("he.?o", txt)
print(x)
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

ex9
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o": ['hello']
x = re.findall("he.{2}o", txt)
print(x)

ex10
import re
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays": ['falls']
#Yes, there is at least one match!
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
