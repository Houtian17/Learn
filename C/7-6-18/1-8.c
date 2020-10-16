#include <stdio.h>
///打问号！
int main() {

    int c, nb, nt, nl;

    nb = 0;
    nt = 0;
    nl = 0;

    while (c = getchar() != EOF) {
        if (c == ' ')
            ++nb;
        else if (c == '\t')
            ++nt;
        else if (c == '\n')
            ++nl;
    }

    printf("%d %d %d\n", nb, nt, nl);

}
