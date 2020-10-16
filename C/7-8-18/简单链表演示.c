#include <stdlib.h>
#include <stdio.h>

typedef struct _node {
    int value;
    struct _node *next;
} Node;


int main() {

    Node *head = NULL;
    int number;
    do {
        scanf("%d", &number);
        if (number != -1) {
            Node *p = (Node *) malloc(sizeof(Node));
            p->value = number;
            p->next = NULL;
            Node *last = head;
            if (last) {
                while (last->next) {
                    last = last->next;
                }
                last->next = p;
            } else {
                head = p;
            }

        }
    } while (number != -1);

}
