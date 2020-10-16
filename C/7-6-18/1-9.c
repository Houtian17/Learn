#include <stdio.h>

#define NONBLANK 'a'

int main() {

    int c, lastc;

    lastc = NONBLANK;
    while ((c = getchar()) != EOF) {
        if (c != ' ' || lastc != ' ')
            putchar(c);
            lastc = c;
    }


}



