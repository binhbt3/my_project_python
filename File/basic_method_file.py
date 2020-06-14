import os
helloFile = open('F:\\python_execsice\\File\\hello_world.txt')
content = helloFile.readlines()

helloFile.close()
#print(content)

helloFile1 = open('F:\\python_execsice\\File\\hello_world.txt','a')
helloFile1.write('Xin chao Viet Nam\n')
helloFile1.write('Xin chao Viet Nam\n')
helloFile1.write('Xin chao Viet Nam\n')
#content1 = helloFile1.readlines()
helloFile1.close()
#print(content1)
