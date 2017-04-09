from urllib2 import *
test = urlopen("https://www.facebook.com")
print(test.headers.getheader('Content-Type'))