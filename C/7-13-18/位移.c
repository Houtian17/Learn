#include <stdio.h>

int main() {
    unsigned char c = 0xAA;

    printf(" c=%hhx\n",c);
    printf(" c=%hhx\n",(char)~c);
    printf(" c=%hhx\n",(char)-c);
}