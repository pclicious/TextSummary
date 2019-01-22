import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import io
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

f = open('tempResume.txt', 'r+')
f.truncate(0) 
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
    with open('tempResume.txt', 'ab') as f:
        f.write(u''.join(extract_text_from_pdf('PoojaCV.pdf')).encode('utf-8').strip())
# getting text document from file
    fname="C:\\Users\\pochaudh\\Desktop\\python image\\tempResume.txt"
    with open(fname, 'rb') as myfile:
        filetext=myfile.read().decode('utf-8')
    print(summarize(filetext,ratio=0.39))
    