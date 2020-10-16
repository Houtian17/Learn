#include <stdio.h>

int main(){

    int a[10];


    printf("%p\n",&a);
    printf("%p\n",a);
    printf("%p\n",&a[0]);
    printf("%p\n",&a[1]);

    /*
        0061FF08
        0061FF08
        0061FF08
        0061FF0C
    */

}
