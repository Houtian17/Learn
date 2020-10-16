#ifndef _STUDENT_H
#define _STUDENT_H

const int STR_LEN = 20;

typedef struct _student {
    int gender;
    int age;
    char name[];
} Student;

#endif
