#include <stdio.h>
///fahr 华氏度  celsius 摄氏度
///(9.0*celsius)/5.0+32.0 只是转化的公式而已
int main() {

    float fahr,celsius;
    int lower,upper,step;

    lower=0;
    upper=300;
    step=20;

    printf("Celsius Fahr\n");
    celsius=lower;

    while (celsius<=upper){
        fahr=(9.0*celsius)/5.0+32.0;
        printf("%3.0f  %6.1f\n",celsius,fahr);
        celsius=celsius+20;
    }

    return 0;
}