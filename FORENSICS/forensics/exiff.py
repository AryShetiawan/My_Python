from PIL import Image
from PIL.ExifTags import TAGS


def testForExif(imgFile):
    if hasattr(imgFile,  '_getexif'):
        print('%s has exif info')
        return True

def getExifData(imgFileName,  tag=None):
    '''Get embedded EXIF data from image file'''
    try:
        exifData ={}
        print('[+] opening %s looking for %r'%(imgFileName,  tag))
        imgFile = Image.open(imgFileName)
        if testForExif(imgFile):
            info = imgFile._getexif()
            if info:
                for (tag,  value) in info.items():
                    decoded = TAGS.get(tag, tag)
                    exifData[decoded] = value
                exifGPS = exifData['GPSInfo']
                if exifGPS:
                    print('[*] %s contains GPS MetaData'%imgFileName)
        return true
    except Exception,  err:
        pass
#        print('[e] %r\n%s'%(err, imgFile))
