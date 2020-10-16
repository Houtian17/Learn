#include <stdio.h>
#include <string.h>

char *mycpy(char *dst, const char *src) {
    int index = 0;
    while (src[index] != '\0') {
        dst[index] = src[index];
        index++;
    }
    dst[index] = '\0';
    return dst;
}

char *mycpy2(char *dst, const char *src) {
    char *ret = dst;
    while (*src != '\0') {
        *dst = *src;
        dst++;
        src++;
    }
    *dst = '\0';
    return ret;
}


int main() {
    char s1[] = "abc";
    char s2[] = "abc";

    strcpy(s1, s2);

}