#include <stdio.h>
#include <stdlib.h>

struct date {
    int year;
    int month;
    int day;
};


int main() {
    struct date thisday;
    struct date today;

    thisday = (struct date) {2018, 7, 8};

    printf("输入日期格式：年-月-日\n");
    scanf("%d-%d-%d", &today.year, &today.month, &today.day);

    printf("\n这个程序来自%d-%d-%d\n", thisday.year, thisday.month, thisday.day);

    if (today.year % 4 == 0 && today.year % 400 != 0) {
        printf("哇，今年shi闰年\n");
    } else {
        printf("今年bushi闰年\n");
    }
}