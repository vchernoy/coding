#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> r;
    for (int i = 0; i < n; i++) {
        int rating;
        cin >> rating;
        r.push_back(rating);
    }

    vector<int> candies(n, 1);

    for (int i = 1; i < n; i++) {
        if (r[i] > r[i-1]) {
            candies[i] = candies[i-1] + 1;
        }
    }

    for (int i = n-2; i >= 0; i--) {
        if (r[i] > r[i+1]) {
            candies[i] = max(candies[i], candies[i+1] + 1);
        }
    }

    long long tot_candies = 0;
    for (int c : candies) {
        tot_candies += c;
    }

    cout << tot_candies << endl;

    return 0;
}

