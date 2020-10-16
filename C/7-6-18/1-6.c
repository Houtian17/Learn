#include <stdio.h>

///getchar()函数结束遇到限定的字符就停止。
///返回int类型
int main() {
    int c;

    while (c = getchar() != 'a') {
        printf("c:%d\n",c);
    }

    //1a23 ->1
    //12a3 ->12
    //123a ->123

    return 0;
}
