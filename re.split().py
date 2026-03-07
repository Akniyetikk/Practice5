ex1
import re
#Split the string at every white-space character: ['The', 'rain', 'in', 'Spain']
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

ex2
import re
#Split the string at the first white-space character: ['The', 'rain in Spain']
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
