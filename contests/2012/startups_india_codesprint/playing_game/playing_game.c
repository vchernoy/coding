#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ASSERT(c) if (c) {} else {printf(#c"\n"); *((char*)0) = 0;}
//#define ASSERT(c)

#define MAX_N (10000)

char DH[MAX_N+1][MAX_N+1];
char DF[MAX_N+1];

typedef char bool;
static const bool TRUE = 1;
static const bool FALSE = 0;

static bool F(int n) {
    int i;

    ASSERT(n > 0);
    ASSERT(n <= MAX_N);

    if (DF[n] == -1) {
        DF[n] = FALSE;
        for (i = 1; i <= n/2; i++) {
            if (!(F(i) || F(n-i))) {
                DF[n] = TRUE;
                break;
            }
        }
    }

    return DF[n];
}    

int main() {
    int t, T, i, n1, n2, nt;
    bool won;

    memset(DH, -1, sizeof(DH));
    DH[1][1] = 0;
    memset(DF, -1, sizeof(DF));

    scanf("%d\n", &T);
    for (t = 0; t < T; t++) {
        scanf("%d %d\n", &n1, &n2);
        if (n1 > n2) {
            nt = n2;
            n2 = n1;
            n1 = nt;
        }
        for (i = 1; i < n2; i++) {
            F(i);
        }
        won = F(n1) || F(n2);
        if (won) {
            printf("Alice\n");
        } else {
            printf("Bob\n");
        }
    }

    return 0;
}
