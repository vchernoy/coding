
namespace std
{
    template<>
    struct hash<pair<string,string> > {
        std::size_t operator () (const pair<string,string> &p) const {
            hash<string> str_hash;
            auto h1 = str_hash(p.first);
            auto h2 = str_hash(p.second);
            return h1 ^ h2;
        }
    };
}

class Solution {
public:
    unordered_map<pair<string, string>, bool> table;

    bool isMatch(string s, string p) {
        while (true) {
            auto pos = p.find("**");
            if (pos == string::npos) {
                break;
            }
            p = p.erase(pos, 1);
        }

        return matched(s, p);
    }

    bool matched(string s, string p) {
        if (p.size() == 0) {
            return s.size() == 0;
        }
        auto key = std::make_pair(s, p);
        auto it = table.find(key);
        if (it != table.end()) {
            return it->second;
        }

        bool res = false;

        int k = 0;
        while (true) {
            if (k == p.size()) {
                res = k == s.size();
                break;
            }

            char c = p[k];
            if (c == '*') {
                auto p1 = p.substr(k+1);
                for (int i = k; i < s.size(); i++) {
                    if (matched(s.substr(i), p1)) {
                        res = true;
                        break;
                    }
                }
                res = res || matched("", p1);
                break;
            }

            if (k == s.size()) {
                break;
            }

            if (c != '?' && s[k] != c) {
                break;
            }

            k++;
        }

        table[key] = res;
        return res;
    }
};

