picdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pic')
libdir = os.path.join(os.path.abspath(os.path.dirname(__file__)))

if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in13_V4
from PIL import Image,ImageDraw,ImageFont
import logging

logging.basicConfig(level=logging.DEBUG)

class Display:
    def init(self):
        self.font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        self.display = epd2in13_V4.EPD()
        self.display.init()
        self.display.Clear(0xFF)

    def sleep(self):
        self.display.sleep()
    
    def shutdown(self):
        epd2in13_V4.epdconfig.module_exit(cleanup=True)

    def clear(self, color = 0xFF):
        self.display.Clear(color)

    def drawText(self, xy: tuple[float, float], text: str):
        image = Image.new('1', (self.display.height, self.display.width), 255)
        draw = ImageDraw.Draw(image)
        self.display.displayPartBaseImage(self.display.getbuffer(image))
        draw.text(xy, text, font = self.font)