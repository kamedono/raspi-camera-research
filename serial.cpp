/*
  http://d.hatena.ne.jp/rinie/20100823/
  参考にさせていただきました。
 */

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <termios.h>
#include <stdio.h>

#define BAUDRATE B9600
#define MODEMDEVICE "/dev/tty.usbserial-DA00SZ7I"
#define _POSIX_SOURCE 1

volatile int STOP=FALSE;

main() {
        int fd,c, res;
        struct termios oldtio,newtio;
        char buf[255];

        fd = open(MODEMDEVICE, O_WRONLY | O_NOCTTY );
        if (fd <0) {perror(MODEMDEVICE); exit(-1); }

        tcgetattr(fd,&oldtio); /* 現在のポート設定を待避 */

        bzero(&newtio, sizeof(newtio));
        newtio.c_cflag = BAUDRATE | CRTSCTS | CS8 | CLOCAL | CREAD;
        newtio.c_iflag = IGNPAR;
        newtio.c_oflag = 0;

        /* set input mode (non-canonical, no echo,...) */
        newtio.c_lflag = 0;

        newtio.c_cc[VTIME]    = 0;/* キャラクタ間タイマは未使用 */
        newtio.c_cc[VMIN]     = 5;/* 5文字受け取るまでブロックする */

        tcflush(fd, TCIFLUSH);
        tcsetattr(fd,TCSANOW,&newtio);

        buf[0] = 123;
        write(fd, buf, 1);

        tcsetattr(fd,TCSANOW,&oldtio);//設定をもとに戻す
        close(fd);
}
