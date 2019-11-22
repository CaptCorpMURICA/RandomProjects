"""
    Author:         CaptCorpMURICA
    Project:        PDF_Manipulations
    File:           pdfMerger.py
    Creation Date:  11/22/2019, 10:43 AM
    Description:    Combine multiple PDF files into a single PDF to avoid overpaying Adobe for their crappy service.
"""

import os
from PyPDF2 import PdfFileMerger

pdfs = ['0005_001.pdf', '0005_110.pdf', '0005_210.pdf', '0005_318.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open("accounting.pdf", "wb") as f:
    merger.write(f)
    f.close()
