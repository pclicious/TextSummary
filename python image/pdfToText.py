# importing required modules 
import PyPDF2 
# creating a pdf file object 
pdfFileObj = open('PoojaCV.pdf', 'rb')
fname="C:\\Users\\pochaudh\\Desktop\\python image\\tempResume.txt"
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# printing number of pages in pdf file 
print(pdfReader.numPages) 

for i in range(0,pdfReader.numPages):		
	pageObj = pdfReader.getPage(i) 
	print(pageObj.extractText())

    with open(fname, 'a') as myfile:
        filetext=myfile.read()
# creating a page object 
#pageObj = pdfReader.getPage(0) 

# extracting text from page 
#print(pageObj.extractText()) 

#pageObj = pdfReader.getPage(1) 
#print(pageObj.extractText()) 

# closing the pdf file object 
pdfFileObj.close()  