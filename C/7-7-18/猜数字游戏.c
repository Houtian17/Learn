#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(0));
    int a = rand(), x, n = 1, t = 7;
    a %= 100;

    printf("猜一个1~100的整数\n");
    scanf("%d", &x);

    while (x != a && t > 0) {
        if (x > a) {
            printf("猜的数字大了");
        } else {
            printf("猜的数字小了");
        }
        n++;
        t--;
        printf("再试一次吧？你还有:%d\n次机会", t);
        scanf("%d", &x);
    }
    if (n > 0) {
        printf("猜对啦！您一共猜了%d次就猜到了正确答案！", n);
    } else {
        printf("连续7次没有猜中，重来一次吧？？");
    }

    return 0;
}
