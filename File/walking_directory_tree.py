import os

for foldername, subfolders, filenames in os.walk("F:\\python_execsice\\File"):
	print('The folder is' + foldername)
	print('The subfolders in ' + foldername + ' are ' + str(subfolders))
	print('The files in ' + foldername + ' are ' + str(filenames))
	print(" ")


