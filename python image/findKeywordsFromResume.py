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
checklist=["python","VB.Net","java","SQL","Linux","pooja"]
wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
#print("Pairs\n" + str(zip(wordlist, wordfreq)))
for i in range(len(wordlist)):
         print("{",wordlist[i],":",wordfreq[i],"}",end=" | ")
for i in range(len(checklist)):
    for j in range(len(wordlist)):
        wordlist[j]=''.join(ch for ch in wordlist[j] if ch not in exclude)
        checklist[i]=''.join(ch for ch in checklist[i] if ch not in exclude)
        #print(checklist[i].lower())
        if(str(checklist[i].lower())==str(wordlist[j].lower())):
             print(checklist[i].lower(),"found")
             path="C:\\Users\\pochaudh\\Desktop\\python image\\"+str(checklist[i].lower())
             if(os.path.isdir(path)):
                  shutil.copy("PoojaCV.pdf",path)
             else:
                  os.mkdir(path)
                  shutil.copy("PoojaCV.pdf",path)				  
