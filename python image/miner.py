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

def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
 
            text = fake_file_handle.getvalue()
            text=text.replace("'",r"\'")
            yield text

            # close open handles
            converter.close()
            fake_file_handle.close()

def extract_text(pdf_path):
    for page in extract_text_by_page(pdf_path):
        with open('tempResume.txt', 'ab') as f:
            f.write(u''.join(page).encode('utf-8').strip())

if __name__ == '__main__':
        extract_text('PoojaCV.pdf')