# multi threading
import threading
from spider import Spider
from Queue import Queue
from Domain import *
from WebCrawler2 import *
PROJECT_NAME = 'thesite'
HOMEPAGE = 'https://www.google.com'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'

#Define number of threads, say 8
NUMBER_OF_THREADS = 8
queue = Queue() #Queue Set
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links))+ 'Links in the queue')
        create_jobs() #firt take the link from queue file, put it in queue, call crawl function

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
        queue.join()
        crawl()

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        #create a thread
        t = threading.Thread(target=work)
        t.daemon = True # to make it a daemon process
        t.start()

def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

create_workers()
crawl()
