#https://automatetheboringstuff.com/chapter7/

import re
print("EXAMPLE1")
regex_phone_number = re.compile(r'\d\d-\d\d\d-\d\d\d\d')
mo = regex_phone_number.search('My number is 034-954-8551')

if mo != None:
    print('Phone number found: ' + mo.group())
else:
    print("No number was found in the text")


# In some cases, we need to take a part of a text or a number. We can use GROUPING WITH PARENTHESES

print("EXAMPLE2")
regex_phone_number1 = re.compile(r'(\d\d)-(\d\d\d)-(\d\d\d\d)')
mo1 = regex_phone_number1.search('My number is 034-951-8551')

if mo1 != None:
    print('Phone number found: ' + mo1.group())
    print('The first part of number',mo1.group(1))
    print('The second part of number',mo1.group(2))
    print('The third part of number',mo1.group(3))
else:
    print("No number was found in the text")
