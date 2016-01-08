//  Created by Toshiki Higaki on 2016/1/4.
//  Copyright (c) 2016年 TabusaLab. All rights reserved.

// Opencvのステレオ画像処理のリアルタイムサンプルになればいいな

#include <stdio.h>
#include <ctype.h>
#include <time.h>
#include <sys/time.h>
#include <unistd.h>

#include <cv.h>
#include <cvwimage.h>
#include <legacy.hpp>

#include <opencv/highgui.h>

int main(int argc, char **argv){
        cv::WImageBuffer1_b left, right, dst; // 符号なし8ビット, 1チャンネル
        cv::WImageBuffer1_16s dispLeft, dispRight; // 符号付き16ビット, 1チャンネル
        CvStereoGCState *state = cvCreateStereoGCState(16, 2); //距離計測(GC版)用 構造体
        CvSize size;
        const char *winName = "Stereo Correspondence";

        // キャプチャ
        CvCapture *capture = 0;
        IplImage *frame = 0;
        int c;

        double width = 320, height = 240;

        // カメラに対するキャプチャ構造体を作成
        // 引数の一つ目が左カメラ、二つ目が右カメラの番号
        assert(argc == 3);
        captuer_left = cvCreateCameraCapture(argv[1][0]);
        captuer_right = cvCreateCameraCapture(argv[1][1]);


        // キャプチャサイズの設定
        cvSetCaptureProperty(captuer_left, CV_CAP_PROP_FRAME_WIDTH, width);
        cvSetCaptureProperty(captuer_left, CV_CAP_PROP_FRAME_HEIGHT, height);
        cvSetCaptureProperty(captuer_right, CV_CAP_PROP_FRAME_WIDTH, width);
        cvSetCaptureProperty(captuer_right, CV_CAP_PROP_FRAME_HEIGHT, height);

        // ウィンドウ作成。
        const char *winName = "Stereo Correspondence";
        cvNamedWindow(winName, CV_WINDOW_AUTOSIZE);

        while(1)
        {
                // 画像キャプチャ。
                frame_left = cvQueryFrame(captuer_left);
                frame_right = cvQueryFrame(captuer_right);

                // if(c == '\x1b') break;
                //sleep(2);

                left.SetIpl(cvLoadImage(frame_left, 0)); // 入力画像：左
                right.SetIpl(cvLoadImage(frame_right, 0)); // 入力画像：右

                // 領域確保
                size = cvGetSize(left.Ipl());
                dispLeft.Allocate(size.width, size.height);
                dispRight.Allocate(size.width, size.height);
                dst.Allocate(size.width, size.height);

                // 距離計測とスケーリング
                cvFindStereoCorrespondenceGC(left.Ipl(), right.Ipl(), dispLeft.Ipl(), dispRight.Ipl(), state, 0);
                cvConvertScale(dispLeft.Ipl(), dst.Ipl(), -16);

                // 出力画像表示
                cvShowImage(winName, dst.Ipl());
                cvWaitKey(0);

        }

        // 後片付け。
        cvReleaseCapture(&capture);
        cvDestroyWindow("Capture");

        return 0;
}
