#!/usr/bin/env python3.5
from pluggy import app, settings

if __name__ == "__main__":
    port = int(settings.settings['port'])
    debug = int(settings.settings['debug'])
    app.run(debug=debug, port=port)
