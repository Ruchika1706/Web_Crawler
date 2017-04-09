from urlparse import urlparse
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except Exception as e:
        return ''

def get_sub_domain_name(url):
    try:
        #netloc is Network Location Part
        #scheme://netloc/path;parameters?query#fragment.
        print urlparse(url).fragment
        return urlparse(url).netloc
    except Exception as e:
        return ''

