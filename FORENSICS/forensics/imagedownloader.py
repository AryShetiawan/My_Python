import urllib2
from urlparse import urlsplit
from os.path import basename,  join
from bs4 import BeautifulSoup

class ArgumentError(Exception):
    """Thrown when modargs.args encounters a command line format error."""
    pass

def findImages(url=None):
    if url == None:
        raise ArgumentError('URL must be given')
    print('[+] Finding images on {0}'.format(url))
    urlContent = urllib2.urlopen(url).read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags

def downloadImage(imgTag = None):
    if imgTag == None:
        raise ArgumentError('[e] URL must be given')
    try:
        print('Downloading image...')
        imgSrc = imgTag['src']
        print imgSrc
        imgContent = urllib2.urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open(join("images", imgFileName), 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except Exception,  err:
        print('[e] %r'%err)