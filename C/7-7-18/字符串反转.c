#include <stdio.h>
#include <string.h>

#define MAXLINE 1000

/*
int main() {
    char a[20] = {0}, b[20] = {0}, *p1, *p2;
    printf("任意输入一个字符串:\n");

    gets(a);
    p1 = a;
    p2 = b + strlen(a) - 1;
    for (; *p1 != '\0'; p1++, p2--) {
        *p2=*p1;
    }
    *p2='\0';
    printf("string a is:%s\n",a);
    printf("string b is:%s\n",b);
}
*/

void reverse(char* str){
    char* p=str +strlen(str)-1;
    char temp;
    while(str<p){
        temp=*p;
        *p--=*str;
        *str++=temp;
    }
}
int main(){
    char str[MAXLINE];
    printf("请输入一个字符串：\n");
    gets(str);
    reverse(str);
    printf("翻转后的字符串是:%s\n",str);
}