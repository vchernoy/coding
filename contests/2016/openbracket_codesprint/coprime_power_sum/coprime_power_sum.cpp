
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define M (1000000007ull)
#define M_(x) ((x) % M)

// inv = [1, 500000004, 166666668, 250000002, 233333335, 83333334, 23809524, 41666667, 411111114, 850000006, 469696973]

uintmax_t f0(uintmax_t m) {
    return m % M;
}

uintmax_t f1(uintmax_t m) {
    m = m % M;
    return M_(M_(m * M_(m + 1)) * 500000004);
}

uintmax_t f2(uintmax_t m) {
    m = m % M;
    uintmax_t m2 = M_(m * m);
    return M_(M_(m * M_(2 * m2 + 3 * m + 1)) * 166666668);
}

uintmax_t f3(uintmax_t m) {
    m = m % M;
    uintmax_t m2 = (m * m) % M;
    return M_(M_(m2 * M_(m2 + 2 * m + 1)) * 250000002);
}

uintmax_t f4(uintmax_t m) {
    m = m % M;
    uintmax_t m2 = (m * m) % M;
    return M_(M_(m * M_(m2 * M_(6 * m2 + 15 * m + 10) + M - 1)) * 233333335);
}

uintmax_t f5(uintmax_t m) {
    m = m % M;
    uintmax_t m2 = (m * m) % M;
    return M_(M_(m2 * M_(m2 * M_(2 * m2 + 6 * m + 5) + M - 1)) * 83333334);
}

uintmax_t f6(uintmax_t m) {
    m = m % M;
    uintmax_t m2 = (m * m) % M;
    return M_(M_(m * M_(m2 * M_(m2 * M_(6 * m2 + 21 * m + 21) + M - 7) + 1)) * 23809524);
}

uintmax_t f7(uintmax_t m) {
    m = m % M;
    uintmax_t m2 = (m * m) % M;
    return M_(M_(m2 * M_(m2 * M_(m2 * M_(3 * m2 + 12 * m + 14) + M - 7) + 2)) * 41666667);
}

uintmax_t f8(uintmax_t m) {
    m = m % M;
    uintmax_t m2 = (m * m) % M;
    return M_(M_(m * M_(m2 * M_(m2 * M_(m2 * M_(10 * m2 + 45 * m + 60) - 42) + 20) - 3)) * 411111114);
}

uintmax_t f9(uintmax_t m) {
    m = m % M;
    uintmax_t m2 = (m * m) % M;
    return M_(M_(m2 * M_(m2 * M_(m2 * M_(m2 * M_(2 * m2 + 10 * m + 15) + M - 14) + 10) + M - 3)) * 850000006);
}

uintmax_t f10(uintmax_t m) {
    m = m % M;
    uintmax_t m2 = (m * m) % M;
    return M_(M_(m * M_(m2 * M_(m2 * M_(m2 * M_(m2 * M_(6 * m2 + 33 * m + 55) + M - 66) + 66) + M - 33) + 5)) * 469696973);
}

inline uintmax_t p0(uintmax_t x) {
    return 1;
}

inline uintmax_t p1(uintmax_t x) {
    return x % M;
}

inline uintmax_t p2(uintmax_t x) {
    uintmax_t _x = x % M;
    return (_x *_x) % M;
}
    
inline uintmax_t p3(uintmax_t x) {
    uintmax_t _x = x % M;
    uintmax_t _x2 = (_x * _x) % M;
    return (_x *_x2) % M;
}

inline uintmax_t p4(uintmax_t x) {
    uintmax_t _x = x % M;
    uintmax_t _x2 = (_x * _x) % M;
    return (_x2 *_x2) % M;
}
    
inline uintmax_t p5(uintmax_t x) {
    uintmax_t _x = x % M;
    uintmax_t _x2 = (_x * _x) % M;
    return ((_x2 *_x2) % M * _x) % M;
}
    
inline uintmax_t p6(uintmax_t x) {
    uintmax_t _x3 = p3(x);
    return (_x3 * _x3) % M;
}
    
inline uintmax_t p7(uintmax_t x) {
    uintmax_t _x = x % M;
    uintmax_t _x3 = p3(_x);
    return ((_x3 * _x3) % M * _x) % M;
}
    
inline uintmax_t p8(uintmax_t x) {
    uintmax_t _x4 = p4(x);
    return (_x4 * _x4) % M;
}
    
inline uintmax_t p9(uintmax_t x) {
    uintmax_t _x = x % M;
    uintmax_t _x4 = p4(_x);
    return ((_x4 * _x4) % M * _x) % M;
}
    
inline uintmax_t p10(uintmax_t x) {
    uintmax_t _x = x % M;
    uintmax_t _x2 = (_x * _x) % M;
    return p5(_x2);
}

uintmax_t powk(int k, uintmax_t x) {
    uintmax_t p = 1;
    x = x % M;
    for (int i = 0; i < k; i++) {
        p = (p * x) % M;
    }
    return p;
}


uintmax_t pow_sum(int k, uintmax_t m) {
    uintmax_t s = 0;
    for (int i = 1; i <= m; i++) {
        s = (s + powk(k, i)) % M;
    }
    return s;
}


typedef uintmax_t (*Func)(uintmax_t x);
    
Func F[11] = {f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10};
Func P[11] = {p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10};


void test() {
    uintmax_t x = 523179112423;
    for (int i = 0; i <= 10; i++) {
        Func pk = P[i];
        
        uintmax_t r1 = pk(x);
        uintmax_t r2 = powk(i, x);
        
        cout << i << ": " << r1 << " " << r2 << " -- " << (r1 - r2) << endl;
    }
    cout << endl;
    for (int i = 110; i <= 10; i++) {
        Func fk = F[i];
        
        uintmax_t r1 = fk(x);
        uintmax_t r2 = pow_sum(i, x);
        
        cout << i << ": " << r1 << " " << r2 << " -- " << (r1 - r2) << endl;
    }
    cout << endl;
}


Func fk;
Func pk;

uintmax_t m;

inline uintmax_t g(uintmax_t x) {
    uintmax_t t = m / x;
    return ((fk(t) % M) * pk(x)) % M;
}

vector<uintmax_t > s;

inline uintmax_t G(uintmax_t z, int beg, int end) {
    if (beg >= end) {
        return 0;
    }

    uintmax_t r = 0;

    uintmax_t x = s[beg]; // s[end-1];

    uintmax_t z1 = 1;
    if (x <= m / z) {
        z1 = x * z;
        r = g(z1);
    }

    if (beg + 1 == end) {
        return r;
    }

//    if (beg + 2 == end) {
//        return g(s[beg]*z) + g(s[beg+1]*z) - g(s[beg]*s[beg+1]*z);
//    }

    // r += G(z, beg, end-1);
    r += G(z, beg+1, end);
    
    if (x <= m / z) {
        //end -= 1;
        beg += 1;
        while ((end > beg) && (s[end-1] > m / z1)) {
            end -= 1;
        }
        
        r += M - G(z1, beg, end);
    }
    
    return r % M;
}

int main() {
    //test();
    
    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        uintmax_t n, k;
        cin >> n >> k >> m;
        
        fk = F[k];
        pk = P[k];

        s.clear();
        for (int j = 0; j < n; j++) {
            uintmax_t sj;
            cin >> sj;
            s.push_back(sj);
        }

        sort(s.begin(), s.end());

        while (!s.empty() && s.back() > m) {
            s.pop_back();
        }

        if (!s.empty() && (s[0] == 1)) {
            cout << 0;
            continue;
        }

        uintmax_t res = M + fk(m) % M - G(1, 0, s.size());
        res = res % M;
        res += M;
        res = res % M;

        cout << res << endl;
    }
    return 0;
}


