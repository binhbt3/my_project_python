import PyPDF2
import os
# Dowload pdf sample file in this link: http://autbor.com/meetingminutes1.pdf

os.chdir("F:\\python_execsice\\Reading pdf")
pdfFile = open('meetingminutes1.pdf', 'rb')

reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)
page = reader.getPage(1)
print(page.extractText())


