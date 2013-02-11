from PIL import Image
from PIL.ExifTags import TAGS


def testForExif(imgFile):
    print dir(imgFile)
    print(imgFile.__dict__)
    if hasattr(imgFile,  '_getexif'):
        print('%s has exif info')
        return True

def getExifData(imgFileName,  tag=None):
    '''Get embedded EXIF data from image file'''
    try:
        exifData ={}
        print('[+] opening %s'%imgFileName)
        imgFile = Image.open(imgFileName)
        if testForExif(imgFile):
            print("\t[*] Got EXIF")
            info = imgFile._getexif()
            if info:
                print("\t[*] Got INFO")
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
