/*
    http://rest-term.com/archives/1072/
    参考にさせていただきました。
 */
// 距離計測（グラフカット）

 #include <cv.h>
 #include <highgui.h>
 #include <cvwimage.h>
 #include <legacy.hpp>

int main(int argc, char **argv) {
        cv::WImageBuffer1_b left, right, dst; // 符号なし8ビット, 1チャンネル
        cv::WImageBuffer1_16s dispLeft, dispRight; // 符号付き16ビット, 1チャンネル
        CvStereoGCState *state = cvCreateStereoGCState(16, 2); //距離計測(GC版)用 構造体
        CvSize size;
        const char *winName = "Stereo Correspondence";

        assert(argc == 3);
        left.SetIpl(cvLoadImage(argv[1], 0)); // 入力画像：左
        right.SetIpl(cvLoadImage(argv[2], 0)); // 入力画像：右
        // 領域確保
        size = cvGetSize(left.Ipl());
        dispLeft.Allocate(size.width, size.height);
        dispRight.Allocate(size.width, size.height);
        dst.Allocate(size.width, size.height);

        // 距離計測とスケーリング
        cvFindStereoCorrespondenceGC(left.Ipl(), right.Ipl(), dispLeft.Ipl(), dispRight.Ipl(), state, 0);
        cvConvertScale(dispLeft.Ipl(), dst.Ipl(), -16);

        // 出力画像表示
        cvNamedWindow(winName, CV_WINDOW_AUTOSIZE);
        cvShowImage(winName, dst.Ipl());
        cvWaitKey(0);

        cvReleaseStereoGCState(&state);
        cvDestroyAllWindows();
        return 0;
}
