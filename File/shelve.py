
import shelve
import os
shelveFile = shelve.open('mydata')
shelveFile['cat']=['meo con', 'meo me', 'meo bo']
print(shelveFile['cat']
