from os import path
from nose.tools import *
from forensics import imagedownloader,  exiff

def setup():
    print("SETUP!")

def teardown():
    print("TEARDOWN!")

def test_basic():
    print("IT RAN!")

TEST_URL = "http://www.flickr.com/photos"

@raises(imagedownloader.ArgumentError)
def test_findImage_call():
    imagedownloader.findImages()

def test_return():
    img = imagedownloader.findImages(TEST_URL)
    assert len(img)>0

@raises(imagedownloader.ArgumentError)
def test_downloadImage_call():
    imagedownloader.downloadImage()

def test_return():
    file_name = imagedownloader.downloadImage(imagedownloader.findImages(TEST_URL)[1])
    assert file_name != ""

def test_fileName():
    file_name = imagedownloader.downloadImage(imagedownloader.findImages(TEST_URL)[1])
    assert path.exists(path.join('images', file_name))

def _testExiff():
    result = exiff.getExifData(imagedownloader.downloadImage(imagedownloader.findImages(TEST_URL)[1]))
    assert (result != None)
