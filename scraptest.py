"""
Testes do livro Web Scraping com Python!!!

http://bit.ly/1FncvYE
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Digite a url: ")
html = urlopen(url)
bsobj = BeautifulSoup(html.read(),"html.parser");
#print(bsobj.h1)
print(bsobj)
