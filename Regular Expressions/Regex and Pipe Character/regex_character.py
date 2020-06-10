
import re

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping'
regex = re.compile(r'\d+\s\w+\s\w+')
print(regex.findall(lyrics))


vowelregex = re.compile(r'[ueoaiUEOAI]')
vowelregex1 = re.compile(r'[ueoaiUEOAI]{2}')
print(vowelregex.findall("Robocop eats baby food"))
print(vowelregex1.findall("Robocop eats baby food"))


vowelregex = re.compile(r'[^ueoaiUEOAI]')
vowelregex1 = re.compile(r'[^^ueoaiUEOAI]{2}')
#print(vowelregex.findall("Robocop eats baby food"))
print(vowelregex1.findall("Robocop eats baby food"))
