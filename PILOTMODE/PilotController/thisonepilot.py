import random

class Pilot(object):
    def __init__(self):
        self.heading_present = True
        self.heading_valid = True
        self.heading = 44

def test_case_stub(example_of_test_case):
    if not example_of_test_case:
        print('[+] executing test case')
    else:
        print example_of_test_case

class Mode(object):
    pilot = Pilot()

    def enter(self):
        print('[+] This mode is not yet configured. Sub-class it and implement enter().')
        exit(1)

    def executeTestCase(self,  test_case = test_case_stub):
        print('This is the clever part!!')
        print('By this point we will have added framework and call the test_case directly')
        test_case('running a default test case')

class Engine(object):

    def __init__(self, mode_map):
        self.mode_map = mode_map

    def play(self):
        current_mode = self.mode_map.opening_mode()
        while True:
            print('\n----------')
            next_mode_name = current_mode.enter()
            current_mode = self.mode_map.next_mode(next_mode_name)

class death(Mode):
    quips = [
             'You crashed. You suck at driving a boat',
             'Your sense of direction really needs looking at.',
             'You are lost and run out of fuel. Get your act together',
             'You found the rocks you were looking for and run aground',
             'Your vessel is not equipped to be at sea and sinks']

    def enter(self,  test_case = test_case_stub):
        print random.choice(self.quips)
        exit(1)

class standBy(Mode):

    def enter(self,  test_case=test_case_stub):
        print('''
You have the helm.
You must successfully navigate the pilot modes and steer your crew to safety.
Whilst switching modes to accomplish your mission you will be required to generate tests to ensure
survival and the correct operation of your pilot.

You reach open water and survey the horizon for safe passage and a welcoming destination
''')
        self.executeTestCase() # returned mode or query existing? query might allow alarm & fault handling
#        Mode = self.executeTestCase(test_case)  # similar thoughts
        action = raw_input('>')
        if action == 'auto':
            if not self.pilot.heading_present:
                print('''
                You attempt to put your vessel into Auto only to realise your compass was damaged in the last storm.
                With no system to safely direct the craft it moves on into the sunset.
                ''')
                return 'death'
            elif self.pilot.heading_present and not self.pilot.heading_valid:
                print('''
                You aimlessly keep pressing auto while looking at your defunct compass. Thinking that you need a new one really bad
                you give up and throw yourself to the fishes
                ''')
                return('death')
            elif self.pilot.heading_present and self.pilot.heading_valid:
                print('''
Everything went okay. Pilot is in auto and you can go for a cup of tea
''')
                return 'auto'

        elif action == 'standby':
            print('''\r
Demonstrating no ability to use the pilot, you spend the rest of your life at the helm.
''')
            return 'standby'

        elif action == 'windVane':
            print('''\r
Ditching all your fuel to be powered by nature wasn't such a good idea.
failing to put the pilot into auto first allows the pilot to ignore your request.
You watch with a glum face as the fuel washes away with the marine life.
''')
            return 'death'

        else:
            print('Not a valid input')
            return 'standby'

class auto(Mode):

    def enter(self,  test_case = test_case_stub):
        print('''\r
You sail along enjoying the day.
Suddenly you require to change course in order to avoid the friendly dolphin directly in front of you.
If you do not do this the rest of the pod will be very unhappy.
''')

        action = raw_input('manouevre>')

        if action == 'standby':
            print('''\r
Fearing the wrath of the pod and failing to identify intrinsic pilot features,
you select the big red standBy button.
You take control of the helm and steer around the dolphin.
''')
            return 'standby'
        elif action == 'auto':
            print('''\r
You confidently press the auto button and wait for action.
Nothing happens and you turn the dolphin into Sushi.
You settle down with a pimms and keep enjoying the day
''')#The pod systemattically take your hull apart and eat you as your vessel sinks. (kept text)
            return 'auto'
        elif action in['+1','+10', '-1','-10']:
            print('''\r
You make the course adjustment and look over the side to see if you missed
''')
            self.pilot.heading = eval('self.pilot.heading '+action)
            print('Heading is now', self.pilot.heading)
            return 'auto'
        elif action == 'dodge':
            return 'dodge'
        else:
            print('Not a valid input')
            return'auto'

class fault(Mode):

    def enter(self,  test_case = test_case_stub):
        pass

class alarm(Mode):

    def enter(self,  test_case = test_case_stub):
        pass

class dodge(Mode):

    def enter(self,  test_case = test_case_stub):
        print('''
Expecting your pilot to deal with this scenario certainly was a mistake.
You find out this feature was removed by Raymarine and your pilot goes out
of control.''')
        return 'death'

class map(object):
    modes = {
             'standby' : standBy(),
             'auto' : auto(),
             'fault' : fault(),
             'alarm' : alarm(),
             'dodge' : dodge(),
             'death' : death()
             }

    def __init__(self, start_mode):
        self.start_mode = start_mode

    def next_mode(self, mode_name):
        return map.modes.get(mode_name)

    def opening_mode(self):
        return self.next_mode(self.start_mode)


a_map = map('standby')
a_game = Engine(a_map)
a_game.play()
