#include <stdio.h>
#include <math.h>

#define FALSE (0)
#define TRUE (1)

typedef int bool_t;

static bool_t prime(int num) {
    int x, max_x;

    x = 7;
    max_x = (int)sqrt(num);
    while (x <= max_x) {
        if (num % x == 0) {
            return FALSE;
        }
        x += 4;
        if (num % x == 0) {
            return FALSE;
        }
        x += 2;
        if (num % x == 0) {
            return FALSE;
        }
        x += 4;
        if (num % x == 0) {
            return FALSE;
        }
        x += 2;
        if (num % x == 0) {
            return FALSE;
        }
        x += 4;
        if (num % x == 0) {
            return FALSE;
        }
        x += 6;
        if (num % x == 0) {
            return FALSE;
        }
        x += 2;
        if (num % x == 0) {
            return FALSE;
        }
        x += 6;
    }
    return TRUE;
}

int main() {
    int steps[] = {4,2,4,2,4,6,2,6};
    bool_t prime_set[80] = {0};
    int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79};
    int i, num, no_step, digit_sum, m, n;

    for (i = 0; i < sizeof(primes) / sizeof(int); i++) {
        prime_set[primes[i]] = TRUE;
    }

    scanf("%d", &n);

    if (n == 1) {
        num = 2;
    } else if (n == 2) {
        num = 3;
    } else if (n == 3) {
        num = 5;
    } else if (n == 4) {
        num = 7;
    } else {
        no_step = 0;
        i = 4;
        num = 7;
        while (TRUE) {
            m = num;
            digit_sum = 0;
            while (m > 0) {
                digit_sum += m % 10;
                m /= 10;
            }
            if (prime_set[digit_sum] && prime(num)) {
                i += 1;
                if (i > n) {
                    break;
                }
            }
            num += steps[no_step];
            no_step = (no_step + 1) % 8;
        }
    }
    printf("%d\n", num);
}

