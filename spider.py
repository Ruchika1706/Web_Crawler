from urllib2 import urlopen
from  HTMLParser import HTMLParser
from link_finder import LinkFinder
from WebCrawler2 import *
from Domain import *
class Spider:
    #set of variables which contain data which is shared among multiple spiders for multithreading
    #shared data between multiple instances of spider class
    project_name = ''
    base_url = '' # so that they do not visit the same URL again
    domain_name = '' #we want to visit the links on one website and not the links belonging to other website, so comapre domain_name
    queue_file = '' #Files in queue to be crawled
    crawled_file = '' # Already crawled file
    queue = set() #set for queue file
    crawled = set() #set for crawled file
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + "/queue.txt"
        Spider.crawled_file = Spider.project_name + "/crawled.txt"
        # boot up the Spider
        self.boot() # boot() is creation of project, make directory  and relevant files (queue.txt and crawled.txt)
        self.crawl_page('First Spider', Spider.base_url) #start crawling of the page, crawl next pages

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_text_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        #check if url not already crawled
        if page_url not in Spider.crawled:
            print (thread_name + "Crawling " + page_url)
            print ('Queue' + str(len(Spider.queue))+ " | Crawled" + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = '' # variable to parse the crawled page
        try:
            response = urlopen(page_url)
            #check content type is html/text, do not open pdf etx file
            if 'text/html' in response.headers.getheader('Content-Type'):
                html_bytes = response.read() #output is in html bytes
                html_string = html_bytes.decode('utf-8','replace') #utf 8 is the encoding format
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url):
                #we dont want to do anything
                continue
            Spider.queue.add(url)

    #make updates to the files, as the sets are used.
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)









