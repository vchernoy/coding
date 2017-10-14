
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdint>
#include <unordered_map>

using namespace std;


const uintmax_t M = 1000000007;
//vector<uint32_t> FT;
unordered_map<uintmax_t, uint32_t> FM;

// F(10**14) = 264301918 

static inline uint32_t Fib(uintmax_t n) {
    //if (n <= 1) {
    //    return n;
    //}
    
    //if ((n < FT.size()) && (FT[n] > 0)) {
    //    return FT[n];
    //}

    auto it = FM.find(n);
    if (it != FM.end()) {
        return it->second;
    }
    
    uintmax_t r;
    if ((FM.find(n-1) != FM.end()) || (FM.find(n-2) != FM.end())) {
        r = (Fib(n-2) + Fib(n-1)) % M;
        FM[n] = r;
        return r;
    }

    uintmax_t k = (n+1)/2;
    uintmax_t fk1 = Fib(k-1);
    uintmax_t fk = Fib(k);

    if (n % 2 == 0) {
        r = ((2*fk1 + fk) % M * fk) % M;
    } else {
        r = ((fk*fk)%M + (fk1*fk1)%M) % M;
    }
    
    //if (n < FT.size()) {
    //    FT[n] = r;
    //}
    FM[n] = r;

    return r;
}
    
vector<uintmax_t> S;
vector<uintmax_t> FS;
vector<uintmax_t> FS1;

static inline uintmax_t Do(int N) {
    //return 0;
    uintmax_t r = 0;
    uintmax_t X0 = 0;
    uintmax_t X1 = 0;
    for (int L=N-1; L>=0; L--) {
        int R = L+1;
        X0 = (X0 + FS[R]) % M;
        X1 = (X1 + FS1[R]) % M;

        uintmax_t Y0 = (X0 * FS1[L]) % M;
        uintmax_t Y1 = (X1 * FS[L]) % M;

        uintmax_t Fs = (M + Y0 - Y1) % M;
        if (S[L] % 2 == 1) {
            Fs = (Fs * (M-1)) % M;
        }

        r = (r + Fs) % M;
    }
            
    return r;
}

vector<uintmax_t> A;

static const int Nmax = 100000;

int main() {
    //FT.resize(12*10000000, 0);
    FM.reserve(30*1000000);
    
    A.reserve(Nmax);
    S.reserve(Nmax+1);
    FS.reserve(Nmax+1);
    FS1.reserve(Nmax+1);

    FM[0] = 0;
    FM[1] = 1;
    FM[2] = 1;
        
    int Q;
    cin >> Q;
    for (int q=0; q<Q; q++) {
        int N;
        cin >> N;
        A.resize(N);
        for (int i=0; i<N; i++) {
            uintmax_t a;
            cin >> a;
            A[i] = a;
        }

        S.resize(N+1);
        FS.resize(N+1);
        FS1.resize(N+1);

        S[0] = 0;
        FS[0] = Fib(0);
        FS1[0] = Fib(1);
        for (int i=0; i<N; i++) {
            uintmax_t s = S[i] + A[i];
            S[i+1] = s;
            FS[i+1] = Fib(s);
            FS1[i+1] = Fib(s+1);
        }
        
        uintmax_t r = Do(N);
        cout << r << endl;
    }
    return 0;
}

