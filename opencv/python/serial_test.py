# -*- coding: utf-8 -*-
#
#    ttp://coniglio.hateblo.jp/entry/20130308
#    参考にさせていただきました。
#

# 7E 00 14 10 01 00 00 00 00 00 00 00 00 FF FE 00 00 61 61 61 61 61 61 AB
# cu.usbserial-DA00T2BX

import time
import serial
import binascii

from xbee import XBee
from xbee.frame import APIFrame
from xbee.python2to3 import byteToInt, intToByte

PORT = '/dev/cu.usbserial-DA00T2BX'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = XBee(ser, escaped=True)

# DEST_ADDR_LONG = "\x00\x13\xA2\x00\x40\x8B\x35\xAE"

# data = "7E 00 7D 33 10 01 00 00 00 00 00 00 00 00 FF FE 00 00 61 61 61 61 61 0C"
HADER = '\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFE\x00\x00'
data = '\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFE\x00\x00\x61\x61\x61\x61\x61\x61\x61'


if __name__ == "__main__":
    while True:
        try:
            frame = APIFrame(data, True)
            send_data = ''.join(['%x' % ord(s) for s in frame.output()])
            s2 = binascii.b2a_hex(frame.output())
            print s2

            ser.write(frame.output())
            # print frame
    #        print "send data"
            # xbee.tx_long_addr(frame='10', dest_addr=DEST_ADDR_LONG, data='A')
            # print xbee.api_commands.frame
    #        xbee.Send(bytearray.fromhex("7E 00 14 10 01 00 00 00 00 00 00 00 00 FF FE 00 00 61 61 61 61 61 61 AB"))
    #        ser.write("\x7E\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFE\x00\x00\x61\x61\x61\x61\x61\x61\xAB")

            # ch = checksum(data)
            # print '%x ' % ord(ch)

            time.sleep(1)
        except KeyboardInterrupt:
            break

    ser.close()
