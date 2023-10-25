from pyfirmata import Arduino, util,STRING_DATA
from time import strftime
import time 

port = 'COM5'

board=Arduino(port)

data="Digital Clock"

while True:
    string = strftime('%I: %M : %S %P')
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(string))
    time.sleep(1)
