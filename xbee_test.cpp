#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <xbee.h>
#include <unistd.h>

void myCB(struct xbee *xbee, struct xbee_con *con, struct xbee_pkt **pkt, void **data) {
        if ((*pkt)->dataLen <= 0) return;

        /* tell the observer what we received */
        printf("rx: [%s]\n", (*pkt)->data);

        /* return the message to the other XBee */
        printf("tx: %d\n", xbee_connTx(con, NULL, (*pkt)->data, (*pkt)->dataLen));
}

int main(void) {
        struct xbee *xbee;
        struct xbee_con *con;
        struct xbee_conAddress address;

        /* setup libxbee, using a Series 1 XBee, on /dev/ttyUSB0, at 57600 baud */
        xbee_setup(&xbee, "xbee1", "/dev/ttyUSB0", 9800);

        /* setup a 64-bit address */
        memset(&address, 0, sizeof(address));
        address.addr64_enabled = 1;
        address.addr64[0] = 0x00;
        address.addr64[1] = 0x13;
        address.addr64[2] = 0xA2;
        address.addr64[3] = 0x00;
        address.addr64[4] = 0x40;
        address.addr64[5] = 0x08;
        address.addr64[6] = 0x18;
        address.addr64[7] = 0x26;

        /* create a 64-bit data connection with the address */
        xbee_conNew(xbee, &con, "64-bit Data", &address);

        /* setup a callback to keep both the system load and response time low */
        xbee_conCallbackSet(con, myCB, NULL);

        /* sleep for a minute! */
        sleep(60);

        /* close the connection */
        xbee_conEnd(con);

        /* shutdown libxbee */
        xbee_shutdown(xbee);

        return 0;
}
