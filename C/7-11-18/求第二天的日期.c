#include <stdio.h>
#include <stdbool.h>

struct date {
    int month;
    int day;
    int year;

};

int numberOfDays(struct date d) {
    int days;
    const int daysPerMonth[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    if (d.month == 2 && isLeap(d))
        days = 29;
    else
        days = daysPerMonth[d.month - 1];

    return days;

}

int isLeap(struct date d) {
    bool leap = false;

    if ((d.year % 4 == 0 && d.year % 400 != 0) || d.year % 400 == 0)
        leap = true;

    return leap;
}

int main() {
    struct date today, tomorrow;

    printf("Enter today's date (mm dd yy):");
    scanf("%i %i %i", &today.month, &today.day, &today.year);

    if (today.day != numberOfDays(today)) {
        tomorrow.day = today.day + 1;
        tomorrow.month = today.month;
        tomorrow.year = today.year;
    } else if (today.month = 12) {
        tomorrow.day = 1;
        tomorrow.month = 1;
        tomorrow.year = today.year + 1;
    } else {
        tomorrow.day = 1;
        tomorrow.month = today.month + 1;
        tomorrow.year = today.year;
    }

    printf("Tomorrow's date is %i-%i-%i.\n", tomorrow.year, tomorrow.month, tomorrow.day);

    return 0;
}