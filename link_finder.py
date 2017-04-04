#import htmlparser to extract links from html page
from html.parser import HTMLParser
from urllib import parse
class LinkFinder(HTMLParser): # Inherit all functions from HTMlparser
    def __init__(self, baseurl, pageurl):
        super.__init()
        self.baseurl = baseurl
        self.pageurl = pageurl
        self.links = set() # declare as a set of links
    #to handle any errror
    def error(self, message):
        pass
    #handle_starttag is an inbuilt function used to handle the start of any tag
    #<a> tags stand for link
    def handle_starttag(self, tag, attrs):
        print(tag)
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.baseurl, value) #Make Complete URL
                    self.links.add(url) #Add it to the set of URLs

    def page_links(self):
        return self.links

