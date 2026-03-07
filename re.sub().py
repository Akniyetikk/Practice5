ex1
import re
#Replace all white-space characters with the digit "9": The9rain9in9Spain
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

ex2
import re
#Replace the first two occurrences of a white-space character with the digit 9: The9rain9in Spain
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

