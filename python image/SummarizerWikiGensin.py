import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
 
import requests
 
# getting text document from Internet
text = requests.get('http://rare-technologies.com/the_matrix_synopsis.txt').text
 
 
#getting text document from file
fname="C:\\Users\\pochaudh\\Desktop\\python image\\demo.txt"
with open(fname, 'r') as myfile:
      text=myfile.read()
     
     
#getting text document from web, below function based from 3
from bs4 import BeautifulSoup
from urllib.request import urlopen
 
def get_only_text(url):
 """ 
  return the title and the text of the article
  at the specified url
 """
 page = urlopen(url)
 soup = BeautifulSoup(page, "lxml")
 text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
 return soup.title.text, text    
 
  
print ('Summary:')
print (summarize(text, ratio=0.01))
 
print ('\nKeywords:')
print (keywords(text, ratio=0.01))
 
url="https://en.wikipedia.org/wiki/Deep_learning"
text = get_only_text(url)
 
print ('Summary:')   
print (summarize(str(text), ratio=0.01))
 
print ('\nKeywords:')
 
# higher ratio => more keywords
print (keywords(str(text), ratio=0.01))