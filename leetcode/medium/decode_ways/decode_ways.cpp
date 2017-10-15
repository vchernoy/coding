
class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        if (n == 0) {
            return 0;
        }

        set<string> onedigit, twodigit;
        for (int k = 1; k <= 9; k++) {
            onedigit.insert(std::to_string(k));
        }
        for (int k = 10; k <= 26; k++) {
            twodigit.insert(std::to_string(k));
        }
        vector<int> f(n+1, 0);
        f[0] = 1;
        f[1] = onedigit.count(s.substr(0, 1));
        
        for (int i = 2; i <= n; i++) {
            f[i] = f[i-1] * onedigit.count(s.substr(i-1, 1));
            f[i] += f[i-2] * twodigit.count(s.substr(i-2, 2));
        }
        return f[n];
    }
};

