#coding:utf-8

import binascii
import cv2
import numpy as np

def readFile(filename):
	image = cv2.imread(filename)
    # print image[0][0]

	cv2.imshow('original',image[0][0])
    # res = image.reshape([1024, 1024])
	cv2.waitKey()

    # 画像をbinaryで読み込み
    # f = open(image, "rb")
    # ima = f.read(1)
    # print "%s" % (binascii.hexlify(ima))
    # ima = f.read(1)
    #
    # print "%s" % (binascii.hexlify(ima))

def readCamera():
	cap = cv2.VideoCapture(0) #Videoを利用する
	cap.grab()
	while(cap.isOpened()):
	    ret, frame = cap.read()

	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Gray colorに変換

	    cv2.imshow('frame',gray)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	readFile("../image/test.jpg")
	# readCamera()
