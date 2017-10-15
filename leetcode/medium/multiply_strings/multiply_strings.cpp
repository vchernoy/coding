
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>

using namespace std;

class Solution {
public:
    static const int base = 10;

    string multiply(string num1, string num2) {
        return swapped(str(mul(to_digits(swapped(num1)), to_digits(swapped(num2)))));
    }

    string swapped(string s) {
        string res(s.size(), '0');
        for (auto i=0; i<s.size(); i++) {
            res[i] = s[s.size() - i - 1];
        }
        return res;
    }

    vector<int> to_digits(string s) {
        vector<int> res;
        for (auto c : s) {
            res.push_back(c - '0');
        }
        return res;
    }

    string str(vector<int> digits) {
        string res;
        for (auto d : digits) {
            res += '0' + d;
        }
        return res;
    }

    vector<int> mul(vector<int> digits1, vector<int> digits2) {
        vector<int> res = to_digits("0");
        int i = 0;
        for (auto d : digits1) {
            res = add(res, shift(scalar_mul(d, digits2), i));
            i += 1;
        }
        return res;
    }

    vector<int> scalar_mul(int scalar, vector<int> digits) {
        vector<int> res;
        int carry = 0;
        for (auto d : digits) {
            int x = d * scalar + carry;
            res.push_back(x % base);
            carry = x / base;
        }
        apply_carry(res, carry);
        return res;
    }

    vector<int> shift(vector<int> digits, int ndigits) {
        vector<int> res(ndigits, 0);
        copy(digits.begin(), digits.end(), back_inserter(res));
        return res;
    }

    vector<int> add(vector<int> digits1, vector<int> digits2) {
        vector<int> res;
        auto len = digits1.size() > digits2.size() ? digits1.size() : digits2.size();
        int carry = 0;
        for (auto i = 0; i < len; i++) {
            auto x = carry
                + (i < digits1.size() ? digits1[i] : 0)
                + (i < digits2.size() ? digits2[i] : 0);

            res.push_back(x % base);
            carry = x / base;
        }
        apply_carry(res, carry);
        return res;
    }

private:
    void apply_carry(vector<int>& digits, int carry) {
        while (carry > 0) {
            digits.push_back(carry % base);
            carry /= base;
        }
        while (digits.size() > 1 && digits.back() == 0) {
            digits.pop_back();
        }
    }

};

