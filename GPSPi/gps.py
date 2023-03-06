import pycurl
import certifi
import gpsd
import time
from datetime import datetime
from io import BytesIO

gpsd.connect()

while True:
    packet = gpsd.get_current()
    if packet.lat == 0 and packet.lon == 0:
        continue
    timestamp = datetime.now().timestamp()
    lat=packet.lat
    lon=packet.lon
    url='path.to.your.server/loc.php?date={}&lat={}&lon={}'.format(int(timestamp),round(packet.lat,5),round(packet.lon,5))
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.perform()
    c.close()
    time.sleep(59)