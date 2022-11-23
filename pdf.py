# a pdf file combiner, just type via console - python3 pdf.py file1.pdf file2.pdf ...
# need to install - pip3 install PyPDF2==1.26

import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.writer('super.pdf')

pdf_combiner(inputs)