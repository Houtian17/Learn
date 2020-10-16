#include <stdio.h>
#include <string.h>

int mycmp(const char *s1, const char *s2) {
    int index = 0;
    while (s1[index] == s2[index] && s1[index] != '\0') {
        /*if (s1[index] != s2[index]) {
            break;
        } else if (s1[index] == '\0') {
            break;
        }*/
        index++;
    }
    /*while (*s1 == *s2 && *s1 != '\0') {
        s1++;
        s2++;
    }*/

    return s1[index] - s2[index];

}

int main() {

    char s1[] = "abc";
    char s2[] = "Abc";
    printf("%d\n", strcmp(s1, s2));


}