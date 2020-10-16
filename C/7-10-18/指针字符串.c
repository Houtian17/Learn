#include <stdio.h>
#include <string.h>
int main() {

    int i=0;
    char *str = "hello";
    char *str2="hello";
    char str3[]="hello";

    printf("str=%p\n", str);
    printf("str2=%p\n",str2);
    printf("str3=%p\n",str3);
    str3[0]='C';
    printf("str3[0]=%c\n",str3[0]);
    return 0;
}