ex1
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) 

ex2
#If no matches are found, the value None is returned:
import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
