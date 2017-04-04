#Crawler visits the web page and captures all the links from it and stores it in a file
#Takes saved URLs, visits each one and captures all the links from this as well
#urllib is the libray having all functions related to URLs, urlopen opens a URL given as input
from urllib2 import urlopen
from bs4 import BeautifulSoup

#In Python 3, we use from urllib.request import urlopen

#output is HTML code
html = urlopen("https://www.wikipedia.org")
bsobj = BeautifulSoup(html.read(), "html.parser") #html.parser is the parser we are using
print(bsobj.h1) #include those elements which have h1 tag
print(bsobj.title) # to get the <title> element from the HTML Code

#but the output is not in human readable format, so we use html.read()
#print(html.read())

#Using HTML Parser to parse what we want in code for example Headings: Using BeautifulSoup HTML parser
#sudo pip install beautifulsoup4 or do via Project Interpreter






