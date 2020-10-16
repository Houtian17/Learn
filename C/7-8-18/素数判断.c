#include <stdio.h>

int isprime(long int num);


int main() {

    long int aa = 0;

    while (1 == 1) {
        printf("\n\n输入一个数来确定是不是素数。\n");
        scanf("%d", &aa);

        int p = isprime(aa);

        if(p){
            printf("zhe shi su shu");
        }else{
            printf("zhe bu shi ");
        }
    }

}

int isprime(long int num) {
    int isprime = 1;
    long int x = num;

    for (int i = 2; i < num; i++) {
        long int x = num;
        x %= i;

        if (x == 0) {
            isprime = 0;
            break;
        }
    }
    return (isprime);
}