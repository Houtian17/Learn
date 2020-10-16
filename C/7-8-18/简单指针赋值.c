#include <stdio.h>

void f(int *p);
void g(int k);

int main(){
    int i=6;
    printf("&i=%p\n",&i);
    f(&i);
    g(i);
}

void f(int *p){
    printf("p=%p\n",p);
    printf("*p=%d\n",*p);
    *p=233;
}

void g(int k){
    printf("k=%d\n",k);
}