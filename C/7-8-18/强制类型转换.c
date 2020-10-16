#include <stdio.h>
#include <stdlib.h>

int main(){
    int a=123;
    float b=1.23;

    printf("a=%d\n b=%f\n",a,b);

    (float)a;
    (int)b;

    printf("转换：\n(float)a=%f\n (int)b=%d\n",a,b);

    return 0;
}
