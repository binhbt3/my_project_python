# Download example.xlsx from :http://autbor.com/example.xlsx
# When we work with excel file.We have some concepts:
#workbook = file excel, sheet means in excel file include many sheets
#row and columm, cell
#


import openpyxl
import os

os.chdir('F:\\python_execsice\\Reading_excel')

workbook = openpyxl.load_workbook('example.xlsx')
type(workbook)



#sheet = workbook.get_sheet_by_name('Sheet1')
sheet = workbook["Sheet1"]

type(sheet)

cell = sheet['A1']
print(cell.value)
print(sheet['A2'].value)

print(sheet['B1'].value)

print('Display the first columm A:')

for i in range(1,8):
    print(sheet['A' + str(i)].value)
 

print('Display the first columm B:')

for i in range(1,8):
    print(sheet['B' + str(i)].value)
    
#How to work with a cell
print(sheet.cell(row = 1, column = 2).value)
