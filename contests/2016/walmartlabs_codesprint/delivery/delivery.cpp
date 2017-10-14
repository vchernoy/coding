
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

unordered_map<int, int> Levels;

inline int dist(int u, int v) {
    if (Levels[u] < Levels[v]) {
        int t = u;
        u = v;
        v = t;
    }

    int dl = Levels[u] - Levels[v];
    for (int i = 0; i < dl; i++) {
        u /= 2;
    }

    int l = 0;
    while (v != u) {
        l += 1;
        v /= 2;
        u /= 2;
    }

    return 2*l + dl;
}


int main() {
    int N, M, Q;
    cin >> N >> M >> Q;
    vector<vector<int>> foods;
    for (int i = 0; i < M; i++) {
        int n;
        cin >> n;
        vector<int> arr;
        for (int j = 0; j < n; j++) {
            int x;
            cin >> x;
            arr.push_back(x);
        }
        foods.push_back(arr);
    }
    
    {
        int n = 1;
        for (int level = 0; level < 17; level++) {
            for (int i = 0; i < (1 << level); i++) {
                Levels[n] = level;
                n += 1;
            }
        }
    }
    
    int tot_path = 0;
    int pos = 1;
    for (int i = 0; i < Q; i++) {
        int food, person;
        cin >> food >> person;
        int best_path = 100000000;
        for (auto r : foods[food-1]) {
            int path = dist(pos, r) + dist(r, person);
            best_path = min(path, best_path);
        }
        tot_path += best_path;
        pos = person;
    }
    cout << tot_path << endl;
    return 0;
}


