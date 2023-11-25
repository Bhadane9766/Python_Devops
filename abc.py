import re

name = "hello"
pattern = re.compile(r"hell")

match_result = pattern.fullmatch(name)

if match_result:
    print("String matches the pattern")
else:
    print("String does not match the pattern")
