#include <stdio.h>

struct date {
    int month;
    int day;
    int year;
};

int main() {
    struct date today;
    today = (struct date) {07, 11, 2018};
    struct date day;
    struct date *pDate = &today;
    day = today;
    day.day = 12;
    printf("Today'date is %i-%i-%i.\n", today.year, today.month, today.day);
    printf("Today'date is %i-%i-%i.\n", day.year, day.month, day.day);
    printf("address of today is %p\n", pDate);

}
