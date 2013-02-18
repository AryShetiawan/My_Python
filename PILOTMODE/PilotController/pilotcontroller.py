import pilot
import engine

try:
    test_pilot = pilot.Pilot('central_corridor')
    test_routine = engine.Engine(test_pilot)

    ##if record = 1: start logging etc

    ##for line in testFile.txt_read_etc.txt:
    test_routine.playback()
except Exception, err:
    print repr(err)
