#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jon
#
# Created:     09/02/2013
# Copyright:   (c) Jon 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

class Top(object):
    '''Base class for protection'''
    def __init__(self, name):
        try:
            self.name = name + 1
        except Exception, e:
            print("[e] %r"%e)

class Child(Top):
    '''Child class with protection'''
    def __init__(self, name):
        super(Child, self).__init__(name)


def main():
    c = Child('Jon')

if __name__ == '__main__':
    main()
