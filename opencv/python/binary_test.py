# -*- coding: utf-8 -*-

import binascii

b1 = '\x10\x01\x02\x03\x04\x01\x02\x03\x04\x01\x02\x03\x04\x01\x02\x03\x04'

# binaryを元に戻す
s = binascii.b2a_hex(b1)
print s

# binary化
b2 = binascii.a2b_hex(s)
if b1 == b2:
  print b2

# 文字列を16進数に変換
  str = 'abcdefgABCDEFG'
  hex_str = ''.join(['%x ' % ord(s) for s in str])
  print hex_str

# binary化
  # b2 = binascii.a2b_hex(hex_str)
  # print b2
