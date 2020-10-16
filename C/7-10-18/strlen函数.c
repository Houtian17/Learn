#include <stdio.h>
#include <string.h>

int mylen(const char *s) {
    int index = 0;

    while (s[index] != '\0') {
        index++;
    }
    return index;
}

int main() {

    char line[] = "Hello";

    printf("长度为：%d\n",mylen(line));

    printf("strlen=%lu\n", strlen(line));
    printf("sizeof=%lu\n", sizeof(line));


}

