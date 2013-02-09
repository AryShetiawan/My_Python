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
from sys import exit
from time import sleep

class ExplosionException(Exception): pass

class Thing(object):
    def test(self, hi):
        print("[+] %r"%hi)

def main():
    try:
        a = Thing()
        a.test("Hello")
        i=0
        try:
            while(0):
                try:
                    i+=1
                    if i > 5000:
                        raise ExplosionException("Too High")
                    if i >2000:
                        raise Warning("Quite High %d"%i)

                except Warning, wng:
                    print("[w] %r\r"%wng),
                except Exception, err:
                    print("[e] while loop: %r :: ")%err,
                    raise
                # user wants to quit - store persistent and leave
                except KeyboardInterrupt, irpt:
                    print("[+] Interupted at\t%d"%i)
                    print("[i] You selected\t%r"%irpt)
                    raise
                sleep(0.001)
        except:
            raise
    except Exception, err:
        print("[e] Quit main() \"%r\"")%err

    except KeyboardInterrupt, irpt:
    ##    issue all exit cmds
    ##    wait for threads to join()
        exit("[!] User quit\t\t%r"%irpt)
    finally:
        print("[+] goodbye")

if __name__ == '__main__':
    print("[+] start")
    main()
    print("[+] complete")