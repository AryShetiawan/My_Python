class Mode(object):

    def enter(self):
        print('[+] This mode is not yet configured. Sub-class it and implement enter().')
        exit(1)


class Engine(object):

    def __init__(self, mode_map):
        self.mode_map = mode_map

    def play(self):
        current_mode = self.pilot_map.mode()
        while True:
            print('\n----------')
            next_mode_name = current_mode.enter()
            current_mode = self.mode_map.next_mode(next_mode_name)

class Death(Mode):
    quips = [
             'You crashed. You suck at driving a boat',
             'Your sense of direction really needs looking at.',
             'You are lost and run out of fuel. Get your act together',
             'You found the rocks you were looking for and run aground']

    def enter(self):
        print random.choice(quips)
        exit(1)

class CentralCorridor(Mode):

    def enter(self):
        pass

class LaserWeaponArmory(Mode):

    def enter(self):
        pass

class TheBridge(Mode):

    def enter(self):
        pass

class EscapePod(Mode):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_Mode):
        pass

    def next_Mode(self, Mode_name):
        pass

    def opening_Mode(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
