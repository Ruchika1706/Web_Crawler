#import htmlparser to extract links from html page
from  HTMLParser import HTMLParser
from urlparse import urlparse
from urlparse import urljoin
class LinkFinder(HTMLParser, object): # Inherit all functions from HTMlparser
    def __init__(self, baseurl, pageurl):
        super(LinkFinder, self).__init__()
        self.baseurl = baseurl
        self.pageurl = pageurl
        self.links = set() # declare as a set of links
    #to handle any errror
    def error(self, message):
        pass
    #handle_starttag is an inbuilt function used to handle the start of any tag
    #<a> tags stand for link
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = urljoin(self.baseurl, value) #Make Complete URL
                    self.links.add(url) #Add it to the set of URLs

    def page_links(self):
        return self.links

