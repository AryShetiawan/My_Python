try:
    from time import sleep
    stop = 0
    while not stop:
        try:
            for x in ['|','/','-','\\','|','/','-','\\']:
                print("%s\r"%x),
                sleep(0.001)
        except:
            stop = 1
            print("%s\r"%'*')
    stop = 0
    i=0
    while not stop:
        try:
            print("%d\r"%i),
            sleep(0.0005)
            i+=1
        except:
            stop = 1
    print('[+] complete')
except Exception, err:
    print('[e] error %r'%err)