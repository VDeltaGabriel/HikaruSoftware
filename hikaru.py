from display import Display
import logging

try:
    display = Display()
    display.init()

    display.drawText((0, 0), 'Hikaru v1');
    num = 0
    while (True):
        num = num + 1
        if (num == 10):
            break
    
    display.clear()

except KeyboardInterrupt:
    logging.info('Stopping...')
    display.shutdown()
    exit()