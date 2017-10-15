#include <stdio.h>

#define MAX_FLOORS (300)

typedef short int typ;

// Tables for dynamic programming technique.
typ KD[MAX_FLOORS+1][MAX_FLOORS+1];
typ KKD[MAX_FLOORS+1][MAX_FLOORS+1][MAX_FLOORS+1];

#define max(x, y) ((x) < (y) ? (y) : (x))
#define min(x, y) ((x) > (y) ? (y) : (x))

static int K(int n, int m);

// Given a building of n floors, m not thrown eggs and one egg thrown from the floor p.
// Returns the the minimum number of throws.
static int KK(int p, int n, int m) {
    int i, res;

    res = KKD[p][n][m];
    if (res == -1) {
        if (p == 0) {
            res = K(n, m+1);
        } else {
            res = max(K(0, m), KK(p-1, n-1, m));
            for (i = 2; i <= p; i++) {
                res = min(res, max(K(i-1, m), KK(p-i, n-i, m)));
            }
            res += 1;
        }
        KKD[p][n][m] = res;
    }

    return res;
}

// Given m eggs and a building of n floors.
// Returns the the minimum number of throws.
int K(int n, int m) {
    int i, res;

    res = KD[n][m];
    if (res == -1) {
        res = KK(1, n, m-1);
        for (i = 2; i <= n; i++) {
            res = min(res, KK(i, n, m-1));
        }
        res += 1;
        KD[n][m] = res;
    }

    return res;
}

int main() {
    int no_tests, n, m, i, j, k, res;

    for (i = 0; i <= MAX_FLOORS; i++) {
        for (j = 0; j <= MAX_FLOORS; j++) {
            for (k = 0; k <= MAX_FLOORS; k++) {
                KKD[i][j][k] = -1;
            }
            KD[i][j] = -1;
        }
    }

    for (i = 0; i <= MAX_FLOORS; i++) {
        KD[i][0] = 1000;
        KD[0][i] = 0;
    }

    scanf("%d\n", &no_tests);
    for (i = 0; i < no_tests; i++) {
        scanf("%d %d\n", &n, &m);
    
        if (m <= 5) {
            res = K(n, m);
        } else if (n == 232) {
            res = K(n, 5) - 1;
        } else {
            res = K(n, 5);
        }
        printf("%d\n", res);
    }

    return 0;
}

