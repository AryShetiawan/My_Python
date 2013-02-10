#! /usr/local/Python-2.6.8rc2 python
import optparse
import imagedownloader,  exiff

def main():
    parser = optparse.OptionParser("Usage getGPS.py -u <target url>")
    parser.add_option("-u", dest="url",  type="string", help="Specify url (address)")
    (options, args) = parser.parse_args()
    url = options.url
    if url == None:
        print(parser.usage)
        exit(0)
    else:
        imgTags = imagedownloader.findImages(url)
        for imgTag in imgTags:
            imgFileName = imagedownloader.downloadImage(imgTag)
            exiff.getExifData(imgFileName)

if __name__ == "__main__":
    main()
