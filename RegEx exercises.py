import re

def task1():
    text = input("Enter string for 'a' followed by zero or more 'b's: ")
    print(bool(re.search('^ab*$', text)))

def task2():
    text = input("Enter string for 'a' followed by two to three 'b's: ")
    print(bool(re.search('ab{2,3}', text)))

def task3():
    text = input("Enter string for lowercase joined with underscore: ")
    print(bool(re.search('^[a-z]+_[a-z]+$', text)))

def task4():
    text = input("Enter string for upper case followed by lower case: ")
    print(re.findall('[A-Z][a-z]+', text))

def task5():
    text = input("Enter string for 'a' anything ending in 'b': ")
    print(bool(re.search('a.*b$', text)))

def task6():
    text = input("Enter string to replace space, comma, or dot: ")
    print(re.sub("[ ,.]", ":", text))

def task7():
    text = input("Enter snake_case string to convert to camelCase: ")
    print(re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text))

def task8():
    text = input("Enter string to split at uppercase: ")
    print(re.findall('[A-Z][^A-Z]*', text))

def task9():
    text = input("Enter string to insert spaces between capitals: ")
    print(re.sub(r"(\w)([A-Z])", r"\1 \2", text))

def task10():
    text = input("Enter camelCase string to convert to snake_case: ")
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower())

if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
