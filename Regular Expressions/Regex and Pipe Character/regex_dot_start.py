import re
beginwithhelloregex = re.compile(r'^Hello')
print(beginwithhelloregex.search("Hello there!"))
print(beginwithhelloregex.search('"He said "Hello"'))
