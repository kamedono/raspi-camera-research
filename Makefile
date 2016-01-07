PROG? = main

CXX = g++
LDFLAGS = -I/usr/include/opencv2/legacy/ -I/usr/include/opencv2/ -I/usr/include/opencv -lopencv_calib3d -lopencv_contrib -lopencv_core -lopencv_features2d -lopencv_flann -lopencv_highgui -lopencv_imgproc -lopencv_legacy -lopencv_ml -lopencv_objdetect -lopencv_photo -lopencv_stitching -lopencv_ts -lopencv_video -lopencv_videostab
CPPLAGS = -I/usr/include/opencv

all: main
