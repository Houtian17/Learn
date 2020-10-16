#include <stdio.h>
#include <string.h>
#include <malloc.h>

int main() {
    char s[] = "hello";
    char *p = strchr(s, 'l');
    char c = *p;
    *p = '\0';
    char *t = (char *) malloc(strlen(s) + 1);

    //p = strchr(p + 1, 'l');
    strcpy(t, s);
    printf("%s\n", p);
    free(t);

    return 0;
}
