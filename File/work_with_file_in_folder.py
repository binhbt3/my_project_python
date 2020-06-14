import os

print(os.getcwd())
print('All files and subfolder in this folder\n')
for filename in os.listdir("F:\\python_execsice\\File"):
	print(filename)

print("\nFile name end with .txt\n")
for filename in os.listdir("F:\\python_execsice\\File"):
	if filename.endswith('.txt'):
		print(filename)
