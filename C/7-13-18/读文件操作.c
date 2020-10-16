#include <stdio.h>

int main() {

    FILE *fp = fopen("ddd.in", "r");

    if (fp) {
        int num;
        fscanf(fp, "%d", &num);
        printf("%d\n", num);
        fclose(fp);
    } else {
        printf("File cant be opened\n");
    }

    return 0;
}