#coding: utf-8
#    http://blanktar.jp/blog/2015/07/python-opencv-crop-box.html
#    参考にさせていただきました。

import cv2
import numpy
import sys


FILENAME = sys.argv[1]
orig = cv2.imread(FILENAME)
num = int(sys.argv[2])

def transform_by4(img, points):
	""" 4点を指定してトリミングする。 """

	points = sorted(points, key=lambda x:x[1])  # yが小さいもの順に並び替え。
	top = sorted(points[:2], key=lambda x:x[0])  # 前半二つは四角形の上。xで並び替えると左右も分かる。
	bottom = sorted(points[2:], key=lambda x:x[0], reverse=True)  # 後半二つは四角形の下。同じくxで並び替え。
	points = numpy.array(top + bottom, dtype='float32')  # 分離した二つを再結合。

	width = max(numpy.sqrt(((points[0][0]-points[2][0])**2)*2), numpy.sqrt(((points[1][0]-points[3][0])**2)*2))
	height = max(numpy.sqrt(((points[0][1]-points[2][1])**2)*2), numpy.sqrt(((points[1][1]-points[3][1])**2)*2))

	dst = numpy.array([
			numpy.array([0, 0]),
			numpy.array([width-1, 0]),
			numpy.array([width-1, height-1]),
			numpy.array([0, height-1]),
			], numpy.float32)

	trans = cv2.getPerspectiveTransform(points, dst)  # 変換前の座標と変換後の座標の対応を渡すと、透視変換行列を作ってくれる。
	return cv2.warpPerspective(img, trans, (int(width), int(height)))  # 透視変換行列を使って切り抜く。


if __name__ == '__main__':

	while cv2.waitKey(10) == -1:

		lines = orig.copy()

		# 輪郭を抽出する
		canny = cv2.cvtColor(orig, cv2.cv.CV_BGR2GRAY)
		canny = cv2.GaussianBlur(canny, (5, 5), 0)
		canny = cv2.Canny(canny, 64, 256)
		cv2.imshow('canny', canny)

		cnts = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]  # 抽出した輪郭に近似する直線（？）を探す。
		cnts.sort(key=cv2.contourArea, reverse=True)  # 面積が大きい順に並べ替える。

		warp = None
		arclen = cv2.arcLength(cnts[num], True)
		approx = cv2.approxPolyDP(cnts[num], 0.001*arclen, True)

		# level = 1 - float(i)/len(cnts)  # 面積順に色を付けたかったのでこんなことをしている。
		if len(approx) == 4:
			cv2.drawContours(lines, [approx], -1, (0, 0, 255), 2)
			if warp == None:
				warp = approx.copy()  # 一番面積の大きな四角形をwarpに保存。
		else:
			cv2.drawContours(lines, [approx], -1, (0, 255, 0), 2)

		# for pos in approx:
			# cv2.circle(lines, tuple(pos[0]), 4, (255, 0, 0))

		cv2.imshow('edge', lines)

		if warp != None:
			warped = transform_by4(orig, warp[:,0,:])  # warpが存在した場合、そこだけくり抜いたものを作る。
			cv2.imshow('warp', warped)

	cv2.destroyAllWindows()
