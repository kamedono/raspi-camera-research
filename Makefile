CXX = g++
CXXFLAGS = \
-I/usr/local/include \
-I/usr/local/include/opencv \
-I/usr/local/include/opencv2 \


LDFLAGS = \
-L/usr/local/lib/opencv \
-L/usr/local/lib/gcc \
-lc++ \
-lopencv_highgui \
-lopencv_core \
-lopencv_ml \
-lopencv_objdetect \
-lopencv_features2d \
-lopencv_imgproc \
-lopencv_video \
-lopencv_videoio \
-lopencv_videostab \
-lopencv_photo \
-lopencv_calib3d \
-lopencv_imgproc \
-lopencv_ml \
-lopencv_stitching \
-lopencv_ts \

all: main
