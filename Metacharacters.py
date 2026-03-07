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

#Flags:
#re.ASCII	re.A	Returns only ASCII matches	
#re.DEBUG		Returns debug information	
#re.DOTALL	re.S	Makes the . character match all characters (including newline character)	
#re.IGNORECASE	re.I	Case-insensitive matching	
#re.MULTILINE	re.M	Returns only matches at the beginning of each line	
#re.NOFLAG		Specifies that no flag is set for this pattern	
#re.UNICODE	re.U	Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches	
#re.VERBOSE	re.X	Allows whitespaces and comments inside patterns. Makes the pattern more readable

ex11
import re
txt = "Åland"
#Find all ASCII matches:
print(re.findall("\w", txt, re.ASCII))
#Without the flag, the example would return all character:
print(re.findall("\w", txt))
#Same result using the shorthand re.A flag:
print(re.findall("\w", txt, re.A))

ex12
import re
txt = "The rain in Spain"
#Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall("spain", txt, re.DEBUG))

#RESULT:
#LITERAL 115
#LITERAL 112
#LITERAL 97
#LITERAL 105
#LITERAL 110

 #0. INFO 16 0b11 5 5 (to 17)
  #    prefix_skip 5
   #   prefix [0x73, 0x70, 0x61, 0x69, 0x6e] ('spain')
    #  overlap [0, 0, 0, 0, 0]
#17: LITERAL 0x73 ('s')
#19. LITERAL 0x70 ('p')
#21. LITERAL 0x61 ('a')
#23. LITERAL 0x69 ('i')
#25. LITERAL 0x6e ('n')
#27. SUCCESS
#[]

ex13
import re
txt = """Hi
my
name
is
Sally"""
#Search for a sequence that starts with "me", followed by one character, even a newline character, and continues with "is": ['me\nis']
print(re.findall("me.is", txt, re.DOTALL))
#This example would return no match without the re.DOTALL flag: []
print(re.findall("me.is", txt))
#Same result with the shorthand re.S flag: ['me\nis']
print(re.findall("me.is", txt, re.S))

ex14
import re
txt = "The rain in Spain"
#Use a case-insensitive search when finding a match for Spain in the text: ['Spain']
print(re.findall("spain", txt, re.IGNORECASE))
#Same result using the shorthand re.I flag: ['Spain']
print(re.findall("spain", txt, re.I))

ex15
import re
txt = """There
aint much
rain in 
Spain"""
#Search for the sequence "ain", at the beginning of a line: ['ain']
print(re.findall("^ain", txt, re.MULTILINE))
#This example would return no matches without the re.MULTILINE flag, because the ^ character without re.MULTILINE only get a match at the very beginning of the text: []
print(re.findall("^ain", txt))
#Same result with the shorthand re.M flag: ['ain']
print(re.findall("^ain", txt, re.M))

ex16
import re
txt = "Åland"
#Find all UNICODE matches: ['Å', 'l', 'a', 'n', 'd']
print(re.findall("\w", txt, re.UNICODE))
#Same result using the shorthand re.U flag: ['Å', 'l', 'a', 'n', 'd']
print(re.findall("\w", txt, re.U))

ex17
import re
text = "The rain in Spain falls mainly on the plain"
#Find and return words that contains the phrase "ain": ['rain', 'Spain', 'mainly', 'plain']
pattern = """
[A-Za-z]* #starts with any letter
ain+      #contains 'ain'
[a-z]*    #followed by any small letter
"""
print(re.findall(pattern, text, re.VERBOSE))
#The example would return nothing without the re.VERBOSE flag: []
print(re.findall(pattern, text))
#Same result with the shorthand re.X flag: ['rain', 'Spain', 'mainly', 'plain']
print(re.findall(pattern, text, re.X))
