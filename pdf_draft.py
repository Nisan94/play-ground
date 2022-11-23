# makes a pdf file with "DRAFT" signature
# need to have wtr.pdf file and any pdf file you want

import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

with open('watermarked_output.pdf', 'wb') as file:
	output.write(file)