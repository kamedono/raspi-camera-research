# -*- coding: utf-8 -*-
import cv2
import time

cap = cv2.VideoCapture(0)  # カメラセット?
i = 0
while(1):
    start = time.clock()  # 開始時刻
    ret, image = cap.read()  # 画像を取得する作業
    get_image_time = int((time.clock() - start) * 1000)  # 処理時間計測
    # 1フレーム取得するのにかかった時間を表示
    cv2.putText(image, str(get_image_time) + "ms", (20, 20), 1, 1, (0, 255, 0))
    cv2.imshow("Camera Test", image)
    # キーが押されたら終了
    if cv2.waitKey(10) == 32:  # 32:[Space]
    cv2.imwrite(str(i) + ".jpg", image)
    i += 1
    print("Save image..." + str(i) + ".jpg")
    elif cv2.waitKey(10) > 27:  # 27:Esc
    cap.release()
    cv2.destroyAllWindows()
    break
