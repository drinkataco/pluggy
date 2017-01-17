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
            self.make_config_files()

        self.conf_loc = open(location, 'r').read()

        config = configparser.ConfigParser()
        config.readfp(open(self.conf_loc + 'settings.conf'))

        for item in config.options('general'):
            self.settings[item] = config.get('general', item)

    def make_config_files(self):
        """
            Make conf location file and copy config files
        """
        print('Welcome to Pluggy!')
        print('In order to set up and allow you to use, we first need a few bits of information from you')
        print('Press enter to select default values. Warning! If configuraton folder location is not changed, all config will be reset on next update')
        
        conf_location    = input('Configuration absolute path: [./conf/] ')
        application_port = input('Application web port: [7373] ')
        application_root = input('Application web root: [/] ')

        # Set defaults if required. Root defaults to blank
        conf_location = conf_location if conf_location else 'conf/'
        application_port = application_port if application_port else 7373

        # create conf_loc file
        conf_loc_file = open('conf_loc', 'w+').write(conf_location)

        # If default location not selected, copy config files into locations
        if conf_location != 'conf/':
            pass

        # Save general settings in settings config
        
        # Print success message to user
        print('Configuration files have been created')
        print('To run pluggy, you can do so straight from the command line')
        print('Or, as we prefer, using Supervisor (see: supervisord.org)')