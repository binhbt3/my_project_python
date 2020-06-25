import pandas as pd
writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')

df = pd.DataFrame({'Name': ['ABC', 'DEF', 'GHI', 'JKL'],
                   'Age': [100, 70, 40, 60]})

# Write data to an excel
df.to_excel(writer, sheet_name="Sheet1", index=False)

# Get workbook
workbook = writer.book

# Get Sheet1
worksheet = writer.sheets['Sheet1']

cell_format = workbook.add_format()
cell_format.set_font_name('Bodoni MT Black')
cell_format.set_font_size(15)

worksheet.set_column('A:H', None, cell_format)

writer.close()
