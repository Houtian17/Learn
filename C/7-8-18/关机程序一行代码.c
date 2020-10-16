#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
    sleep(1);
    system("shutdown -s -f -t 00");
    return 0;
}

