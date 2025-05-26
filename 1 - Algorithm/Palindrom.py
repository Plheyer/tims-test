import re

def palindrom(string):
    string = re.sub(r'[^a-zA-Z0-9]', '', string).lower()
    return string == string[::-1]

string = input("Enter a string:\n")
print(palindrom(string))