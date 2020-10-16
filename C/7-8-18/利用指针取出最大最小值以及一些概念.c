#include <stdio.h>

void minmax(int *a, int len, int *max, int *min); // return int *

int main() {

    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 17, 19, 21, 25, 88, 77, 233};
    int min, max;
    printf("main sizeof(a)=%lu\n", sizeof(a));
    printf("main a=%p\n", a);
    minmax(a, sizeof(a) / sizeof(a[0]), &min, &max);
    printf("min=%d,max=%d\n", min, max);

    int *p=&min;
    printf("*p=%d=\n",*p);
    printf("p[0]=%d\n",p[0]);

    printf("*a=%d\n",*a); //??????为啥*a是10086???

    return 0;
}

void minmax(int *a, int len, int *min, int *max) {
    int i;
    a[0]=10086;
    printf("minmax sizeof(a)=%lu\n", sizeof(a)); //和一个指针的大小是一样的
    printf("main a=%p\n", a);
    printf("minmax");
    *min = *max = a[0];
    for (int i = 1; i < len; i++) {
        if (a[i] < *min) {
            *min = a[i];
        }
        if (a[i] > *max) {
            *max = a[i];
        }
    }

}