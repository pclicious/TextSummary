# Reading an excel file using Python 
import xlrd 
import io
import os
import shutil
import string
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
exclude = set(string.punctuation)

def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
 
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    # close open handles
    converter.close()
    fake_file_handle.close()
	
    if text:
        return text
if __name__ == '__main__':
	wordstring = extract_text_from_pdf('PoojaCV.pdf').encode("utf-8",errors="ignore").strip()
	wordstring = wordstring.decode('utf-8')
	wordlist = wordstring.split()
# Give the location of the file 
loc = ("skillset.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
# For row 0 and column 0 
#data=sheet.cell_value(0, 0) 
rows=int(sheet.nrows)
cols=int(sheet.ncols) 
for i in range(1,rows):
	data1=sheet.cell_value(i, 0)
	print(data1)
	for j in range(1,cols):
		data2=sheet.cell_value(i, j)
		print(data2)
		for k in range(len(wordlist)):
				data1=''.join(ch for ch in data1 if ch not in exclude)
				wordlist[k]=''.join(ch for ch in wordlist[k] if ch not in exclude)
				if(str(data1.lower())==str(wordlist[k].lower())):
					print(data1.lower(),"found")
					if(os.path.isdir(data2)):
						shutil.copy("PoojaCV.pdf",data2)
					else:
						os.mkdir(data2)
						shutil.copy("PoojaCV.pdf",data2)
					