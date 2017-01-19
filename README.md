# Pluggy #

Pluggy allows the controlling of Energenie Mi|Home Sockets and Adapters from a Raspberry Pi with the [Pi-mote Control Board](https://energenie4u.co.uk/catalogue/product/ENER314)

As the Pi-mote control board can only control 4 sockets, Pluggy can callout other devices on the network which also have the software installed.

Actions can be defined to group methods to change the status of several sockets at the same time.

![Pluggy Screenshot](https://raw.githubusercontent.com/drinkataco/pluggy/develop/screenshot.png)

## Requirements ##
Pluggy requires Python3>, and the libraries Flask, request, and gpiozero