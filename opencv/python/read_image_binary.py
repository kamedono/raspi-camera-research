# -*- coding: utf-8 -*-

import time
import serial
import binascii

# 画像をbinaryで読み込み
f = open("../image/test.jpg", "rb")

if __name__ == "__main__":
    while True:
        try:
            ima = f.read(250)
            print "%s" % (binascii.hexlify(ima))

            send_data = ''.join(['%x' % ord(s) for s in ima])
            s2 = binascii.b2a_hex(ima)
            print s2


            time.sleep(0.1)
        except KeyboardInterrupt:
            break

    ser.close()
