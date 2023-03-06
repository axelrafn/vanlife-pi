# GPSPi
This is a project for a GPS logger so I can graph my travels after the fact and show family where I am at any point.

To use this, first install gpsd in your local linux machine and make sure you have a GPS module.
The gps.py file I run on a Raspberry Pi 4 and on the other end I have a LAMP server and I have the loc.php to receive messages from the GPS server.

You can modify the wait time in the gps.py file to your liking. I have it at 1 minute circa so I can have more data than not.