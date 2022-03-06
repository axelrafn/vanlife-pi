import time
import board
import adafruit_sht4x
import busio
import displayio
import terminalio
import microcontroller
from adafruit_display_text import bitmap_label as label
from adafruit_displayio_sh1107 import SH1107, DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297

displayio.release_displays()

i2c = busio.I2C(board.SCL1, board.SDA1)
sht = adafruit_sht4x.SHT4x(i2c)
sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)

WIDTH = 128
HEIGHT = 128
ROTATION = 0

BORDER = 2

display = SH1107(
    display_bus,
    width=WIDTH,
    height=HEIGHT,
    display_offset=DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297,
    rotation=ROTATION,
)

while True:
    temperature, relative_humidity = sht.measurements;
    selfTemp = microcontroller.cpu.temperature;
    # Make the display context
    splash = displayio.Group()
    display.show(splash)

    # Draw some label text
    size_text = "%0.fc" % temperature;
    size_text_area = label.Label(
        terminalio.FONT, text=size_text, scale=3, color=0xFFFFFF, x=38, y=42
    )
    splash.append(size_text_area)
    oled_text = "%0.f%%" % relative_humidity;
    oled_text_area = label.Label(
        terminalio.FONT, text=oled_text, scale=3, color=0xFFFFFF, x=58, y=74
    )
    splash.append(oled_text_area)
    self_text = "%0.f" % selfTemp;
    self_text_area = label.Label(
        terminalio.FONT, text=self_text, scale=1, color=0xFFFFFF, x=115, y=120
    )
    splash.append(self_text_area)
    time.sleep(60)
