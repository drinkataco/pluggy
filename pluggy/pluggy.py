from gpiozero import Energenie
from collections import OrderedDict
import configparser


class Pluggy(object):

    # Location of config files
    conf_loc = ''

    # Plug dictionary (hostname to plugs)
    plugs = {}

    def __init__(self):
        """
            Grab configuration location
        """
        self.conf_loc = '/Users/joshwalwyn/Desktop/conf/'

    def get_channels(self):
        """
            Parse channels configuration file and return
        """
        channels = {}

        config = configparser.ConfigParser()
        config.readfp(open(self.conf_loc + 'channels.conf'))

        for item in config.sections():
            options = {}
            for name in config.options(item):
                options[name] = config.get(item, name)
            channels[item] = options
        print(channels)
        return channels

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
        print(actions)
        return actions

    def get_timers(self):
        """
            Get timers
        """
        pass

    def switch(self, channel, frequency, on):
        """
            Turns swich on/off
            @todo add excetion catching
        """
        print(self.plugs)

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
        pass

    def _external_switch_call(self, channel, frequency, on):
        """
            If external hostname/ip supplied then perform POST callout
        """
        url = channel+'?switch='+str(frequency)+'&on='+str(on)+'&channel=localhost&callout=true'
        print('--CALLOUT--')
        print(url)
