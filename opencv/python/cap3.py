# -*- coding: utf-8 -*-
import cv2
def capture_camera(mirror=True, size=None):
    # カメラをキャプチャする
    cap = cv2.VideoCapture(0)
    # 0はカメラのデバイス番号

    count = 0
    while True:
        # retは画像を取得成功フラグ
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 鏡のように映るか否か
        if mirror is True:
            frame = gray[:,::-1]

        # フレームをリサイズ
        # sizeは例えば(800, 600)
        # if size is not None and len(size) == 2:
        frame = cv2.resize(gray, (200, 150))

        count += 1
        # name = "".join("name", count, ".jpg")
        cv2.imwrite("../image/name%d.jpg" % count, frame)
        # フレームを表示する
        cv2.imshow('camera capture', frame)

        k = cv2.waitKey(1) # 1msec待つ
        if k == 27: # ESCキーで終了
            break

    # キャプチャを解放する
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_camera()
