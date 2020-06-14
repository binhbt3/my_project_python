import shutil
# This function will copy file binhbt3.txt to folder  F:\python_execsice\File\
shutil.copy('F:\\binhbt3.txt','F:\\python_execsice\\File')

# This function will copy file binhbt3.txt to folder  F:\python_execsice\File\ and re name : binhbt3_rename_1.txt
shutil.copy('F:\\binhbt3.txt','F:\\python_execsice\\File\\binhbt3_rename_1.txt')

#Cpoy a folder from F:\\folder_copy to F:\\folder_copy_bakup
#shutil.copytree("F:\\folder_copy", "F:\\folder_copy_bakup")

#Move file from : F:\\account.txt to another place: F:\\python_execsice\\File
#shutil.move('F:\\account.txt','F:\\python_execsice\\File')


#Move file from : F:\\account.txt to another place: F:\\python_execsice\\File and rename
shutil.move('F:\\account.txt','F:\\python_execsice\\File\\account_rename.txt')


