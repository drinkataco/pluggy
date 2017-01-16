from gpiozero import Energenie
import configparser

class Pluggy(object):

    # Location of config files
    conf_loc = ''

    # Plug dictionary (hostname to plugs)
    plugs = {}

    # channels config
    channels = {}

    def __init__(self, location):
        """
            Grab configuration location
        """
        self.conf_loc = location

    def get_channels(self):
        """
            Parse channels configuration file and return
        """

        # only create config if doesn't already exist
        if not bool(self.channels):
            channels = {}

            config = configparser.ConfigParser()
            config.readfp(open(self.conf_loc + 'channels.conf'))

            for item in config.sections():
                options = {}
                for name in config.options(item):
                    options[name] = config.get(item, name)
                channels[item] = options

            self.channels = channels

        return self.channels

    def get_actions(self):
        """
            Parse actions configuration file and return
        """
        actions = {}

        config = configparser.ConfigParser()
        config.readfp(open(self.conf_loc + 'actions.conf'))

        for item in config.sections():
            options = {}
            for name in config.options(item):
                options[name] = config.get(item, name)
            actions[item] = options

        return actions

    def get_timers(self):
        """
            Get timers
        """
        pass

    def switch(self, channel, frequency, on):
        """
            Turns swich on/off
        """
        # create dictionary of data on first runs
        if (channel not in self.plugs):
            self.plugs[channel] = {}

        if (frequency not in self.plugs[channel]):
            if (channel == 'localhost'):
                energenieObject = Energenie(frequency, on)
            else:
                energenieObject = '@ref='+channel
                self._external_switch_call(channel, frequency, on)

            self.plugs[channel][frequency] = energenieObject
            return True;

        # If a string, then this is an external callout
        if (isinstance(self.plugs[channel][frequency], str)):
            self._external_switch_call(channel, frequency, on)
        else:
            if (on):
                self.plugs[channel][frequency].on()
            else:
                self.plugs[channel][frequency].off()

        return True

    def action(self, action):
        """
            Perform defined action
        """
        instructions = action.split('&')
        channels = self.get_channels();

        for instruction in instructions:
            channel = channels[instruction.split(',')[0]]

            # call method
            self.switch(channel['channel'],
                        int(channel['frequency']),
                        int(instruction.split(',')[1]))

        return True

    def _external_switch_call(self, channel, frequency, on):
        """
            If external hostname/ip supplied then perform POST callout
        """
        url = channel+'?switch='+str(frequency)+'&on='+str(on)+'&channel=localhost&callout=true'
        print('--CALLOUT--')
        print(url)