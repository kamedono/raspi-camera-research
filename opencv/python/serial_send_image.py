# -*- coding: utf-8 -*-

import time
import serial
import binascii
import sys

from xbee import XBee
from xbee.frame import APIFrame
from xbee.python2to3 import byteToInt, intToByte

# PORT = '/dev/cu.usbserial-'
BAUD_RATE = 57600
# BAUD_RATE = 9600

# ポートの入力を必須化
if (len(sys.argv) != 3):
    quit()
PORT = sys.argv[1]
FILENAME = sys.argv[2]

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = XBee(ser, escaped=True)

HADER = '\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFE\x00\x00'
END_POINT = '\x7E\x00\x0E\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFE\x00\x00\xF1'

# 画像をbinaryで読み込み
f = open(FILENAME, "rb")

finish_count = 0
send_count = 0

if __name__ == "__main__":

    while True:
        try:
            send_count += 1

            # 480以上の送信は止まるので一旦クローズ
            if send_count % 470 == 0:
                ser.close()
                ser = serial.Serial(PORT, BAUD_RATE)
                # print "stop"
                # send_count = 0

            # データを250byteのみ読み込む
            data = f.read(250)

            # ヘッダーをデータの頭に追加
            data = "".join([HADER, data])

            # xbeeのaipフレームに合わせる
            frame = APIFrame(data, True)
            send_data = ''.join(['%x' % ord(s) for s in frame.output()])

            # 終了かどうか
            if frame.output() == END_POINT:
                finish_count += 1

                print "end point%d" % send_count
                f.close()
                f = open(FILENAME, "rb")
                if finish_count is 5:
                    print "finish"
                    break

            # データを転送
            ser.write(frame.output())
            time.sleep(0.3)
        except KeyboardInterrupt:
            break

    ser.close()
