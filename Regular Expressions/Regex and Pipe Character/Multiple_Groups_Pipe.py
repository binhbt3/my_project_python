#Matching Multiple Groups with the Pipe

import re

nameregex = re.compile(r'Binh|Hong')
mo = nameregex.search('Binh va Hong la doi ban than')
print(mo.group())


# Findall: Find all information, no the first
mo1 = nameregex.findall('Binh va Hong la doi ban than')
print(mo1)


#Optional matching
nameregex1 = re.compile(r'Bat(wo)?man')
mo2 = nameregex1.search('The Adventures of Batman')
print(mo2.group())

nameregex1 = re.compile(r'Bat(wo)?man')
mo2 = nameregex1.search('The Adventures of Batwoman')
print(mo2.group())


#Matching Zero or More with the Star
batRegex =   re.compile(r'Bat(wo)*man')
mo2 = batRegex.search('The Adventures of Batwowowoman')
print(mo2.group())

#Matching One or More with the Plus
batRegex =   re.compile(r'Bat(wo)+man')
mo2 = batRegex.search('The Adventures of Batwowowowowoman')
print(mo2.group())


#Greedy and Nongreedy Matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()







