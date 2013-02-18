class Mode(object):
    '''base class for all mode transitions etc...'''
    def enter(self, logging=False):
        print "[+] This mode is not yet configured. Subclass it and implement enter()."
        exit(1)

    def logTheChange(self):
        def log(*args, **kwargs):
            if self.logging:
                if args or kwargs:
                    #parse the args? pss them to a parser? (lxml,xml <tag> = var...) investigate.
                    raise notImplementedException('logging has not been implemented yet\n(sorry)')
                    self.logger.write(transition)
                else: pass
            else: pass

        try:
            return func(*args, **kwargs)
        except Exception:
            pass
