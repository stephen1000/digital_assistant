

class BaseApp():
    """ Defines the structure for a circuit py application """

    APP_NAME = None

    def __init__(self):
        self.key_mappings = {}

    def start(self):
        """ Defines what happens when an app starts """
        pass

    def stop(self):
        """ Defines what happens when an app stops """
        pass

    def process(self, key):
        """ Processes a predefined input method """
        if key in self.key_mappings:
            self.key_mappings[key]()
