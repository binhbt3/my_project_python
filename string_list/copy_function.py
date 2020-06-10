import copy

spam = ['a','b','c','d']
cheese = copy.deepcopy(spam)
cheese.append('e')
print(spam)

print("\n\n\n")

print(cheese)
