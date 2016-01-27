# -*- coding: utf-8 -*-

import time
import serial
import binascii
import sys

from xbee import XBee
from xbee.frame import APIFrame
from xbee.python2to3 import byteToInt, intToByte

PORT = '/dev/cu.usbserial-'
# BAUD_RATE = 115200
# BAUD_RATE = 111111
BAUD_RATE = 57600
# BAUD_RATE = 9600

# ポートの入力を必須化
if len(sys.argv) < 1:
    portName = "DA00T2BX"

else:
    portName = sys.argv

PORT += portName[1]

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = XBee(ser, escaped=True)

# DEST_ADDR_LONG = "\x00\x13\xA2\x00\x40\x8B\x35\xAE"

HADER = '\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFE\x00\x00'

END_POINT = '\x7E\x00\x0E\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFE\x00\x00\xF1'
# 画像をbinaryで読み込み
f = open("../image/test.jpg", "rb")
count = 0

if __name__ == "__main__":

    while True:
        try:
            data = f.read(250)
            # print "%s" % (binascii.hexlify(data))

            data = "".join([HADER, data])

            frame = APIFrame(data, True)
            send_data = ''.join(['%x' % ord(s) for s in frame.output()])
            s2 = binascii.b2a_hex(frame.output())
            # print s2
            if frame.output() == END_POINT:
                print "end"
                break


            ser.write(frame.output())

            time.sleep(0.3)
        except KeyboardInterrupt:
            break

    ser.close()
