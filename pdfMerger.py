import PyPDF2
import os
import sys

def pdfcombiner(files):
    merger = PyPDF2.PdfFileMerger()
    for pdf in files:
        merger.append(pdf)
    merger.write(os.path.join(infp,'merged.pdf'))

infp = 'C:\\Akash\\LearningDocuments\\Python\\Projects\\PDFProject\\input files\\'
inputs = sys.argv[1:]
files = list()
for input in inputs:
    file = os.path.join(infp,input)
    if os.path.isfile(file) and file.split('.')[1] == 'pdf':
        files.append(file)
    else:
        continue
pdfcombiner(files)



