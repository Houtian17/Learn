#include <stdio.h>
#include <stdlib.h>


int main() {

    int number;
    int *a;

    printf("输入数量：");
    scanf("%d", &number);

    a = (int *) malloc(number * sizeof(int));

    for (int i = 0; i < number; i++) {
        scanf("%d\n", &a[i]);
    }

    for (int i = number - 1; i >= 0; i--) {
        printf("%d\n", a[i]);
    }

    free(a);

    return 0;
}