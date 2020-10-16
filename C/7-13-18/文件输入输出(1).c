#include <stdio.h>
#include "student.h"

void getList(Student aStu[], int number);

int save(Student aStu[], int number);

int main() {
    int number = 0;
    printf("please enter the number for students:\n");
    scanf("%d", &number);
    Student aStu[number];

    getList(aStu, number);

    if (save(aStu, number)) {
        printf("success\n");
    } else {
        printf("fail\n");
    }

    return 0;
}

void getList(Student aStu[], int number) {
    char format[STR_LEN];
    sprintf(format, "%%%ds", STR_LEN - 1);

    int i;
    for (int i = 0; i < number; i++) {
        printf("The %d few student:\n", i);
        printf("\tname:");
        scanf(format, aStu[i].name);
        printf("\tgender:(0-male,1-Female,2-else):");
        scanf("%d", &aStu[i].gender);
        printf("\tage:");
        scanf("%d", &aStu[i].age);
    }
}

int save(Student aStu[], int number) {
    int ret = -1;
    FILE *fp = fopen("student.date", "w");

    if (fp) {
        ret = fwrite(aStu, sizeof(Student), number, fp);
        fclose(fp);
    }

    return ret == number;
}