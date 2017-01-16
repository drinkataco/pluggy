import os
import configparser

class Settings(object):

    # Location of configuration files
    conf_loc = ''

    # General settings
    settings = {}

    def __init__(self):
        """
            Initiate Settings List, or call setup method
        """
        location = os.path.dirname(os.path.realpath(__file__)) + '/../conf_loc'

        if not os.path.exists(location):
            make_config_files()

        self.conf_loc = open(location, 'r').read()

        config = configparser.ConfigParser()
        config.readfp(open(self.conf_loc + 'settings.conf'))

        for item in config.options('general'):
            self.settings[item] = config.get('general', item)

    def make_config_files(self):
        """
            Make conf location file and copy config files
        """
        pass
