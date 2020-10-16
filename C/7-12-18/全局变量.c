#include <stdio.h>

int gAll;

int main() {

    printf("in %s gAll = %d\n", __func__, gAll);
    f();
    printf("agn in %s gAll = %d\n", __func__, gAll);

    return 0;
}


int f(void) {
    printf("in %s gAll=%d\n", __func__, gAll);
    gAll += 2;
    printf("in %s gAll=%d\n", __func__, gAll);

    return gAll;
}