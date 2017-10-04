#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <tuple>
#include <map>
#include <unordered_map>
#include <string>
#include <sstream>
#include <limits.h>

using namespace std;

// Structure to represent an interval
struct Interval {
    int low, high;
    Interval(int l, int h): low(l), high(h) {}
};
 
// Structure to represent a node in Interval Search Tree
struct ITNode {
    Interval i;  // 'i' could also be a normal variable
    int max;
    ITNode* left; 
    ITNode* right;
    ITNode(Interval _i) : i(_i), left(nullptr), right(nullptr), max(_i.high) {}
};
  
// A utility function to insert a new Interval Search Tree Node
// This is similar to BST Insert.  Here the low value of interval
// is used to maintain BST property
static inline ITNode* insert(ITNode* root, const Interval& i) {
    // Base case: Tree is empty, new node becomes root
    if (root == nullptr) {
        return new ITNode(i);
    }
 
    // Get low value of interval at root
    int l = root->i.low;
 
    if (i.low < l) {
        // If root's low value is smaller, then new interval goes to left subtree
        root->left = insert(root->left, i);
    } else {
        // Else, new node goes to right subtree.
        root->right = insert(root->right, i);
    }
    // Update the max value of this ancestor if needed
    if (root->max < i.high) {
        root->max = i.high;
    }
 
    return root;
}
 
// A utility function to check if given two intervals overlap
static inline bool overlap(const Interval& i1, const Interval& i2) {
    return i1.low <= i2.high && i2.low <= i1.high;
}

// The main function that searches a given interval i in a given
// Interval Tree.
static inline Interval* search_overlap(ITNode *root, const Interval& i) {
    // Base Case, tree is empty
    if (root == nullptr) {
        return nullptr;  
    }

    // If given interval overlap with root
    if (overlap(root->i, i)) {
        return &root->i;
    }
 
    // If left child of root is present and max of left child is
    // greater than or equal to given interval, then i may
    // overlap with an interval is left subtree
    if (root->left != nullptr && root->left->max >= i.low) {
        return search_overlap(root->left, i);
    }
    // Else interval can only overlap with right subtree
    return search_overlap(root->right, i);
}


// The main function that searches a given interval i in a given
// Interval Tree.
static inline void all_overlaped(ITNode *root, const Interval& i, vector<Interval>& found) {
    // Base Case, tree is empty
    if (root == nullptr) {
        return;  
    }

    // If given interval overlap with root
    if (overlap(root->i, i)) {
        found.push_back(root->i);
        // return
    }
 
    // If left child of root is present and max of left child is
    // greater than or equal to given interval, then i may
    // overlap with an interval is left subtree
    if (root->left != nullptr && root->left->max >= i.low) {
        all_overlaped(root->left, i, found);
    }
    // Else interval can only overlap with right subtree
    all_overlaped(root->right, i, found);
}

static inline void inorder(ITNode* root) {
    if (root == nullptr) {
        return;
    }
    inorder(root->left);
    cout << "[" << root->i.low << ", " << root->i.high << "]"
         << " max = " << root->max << endl; 
    inorder(root->right);
}

static inline Interval minLowInterval(ITNode* root) {
    while (root->left != nullptr) {
        root = root->left;
    }
    return root->i;
}

static inline int findMax(int high, int max1, int max2) {
    return max(max(high, max1), max2);
}

static inline ITNode* remove(ITNode* root, const Interval& i) {
	if (root == nullptr){
		return nullptr;
	}

	if (i.low < root->i.low){
		root->left = remove(root->left, i);
	} else if (i.low > root->i.low){
		root->right = remove(root->right, i);
	} else if (i.low == root->i.low && i.high == root->i.high){
		if (root->left == nullptr){
			struct ITNode* temp = root->right;
			free(root);
			return temp;
		} else if (root->right == nullptr){
			struct ITNode* temp = root->left;
			free(root);
			return temp;
		}
		Interval minLowI = minLowInterval(root->right);
		root->i = minLowI;
		root->right = remove(root->right, minLowI);
	}
	root->max = findMax(
        root->i.high,
        ((root->left != nullptr) ? root->left->max : INT_MIN),
        ((root->right != nullptr) ? root->right->max : INT_MIN)
    );
	return root;
}

struct itree {
    ITNode* root;
    inline itree() : root(nullptr) {}
    inline void add(Interval i) {
        root = insert(root, i);
    }
    inline void del(Interval i) {
        root = remove(root, i);
    }
    inline Interval* overlaped(Interval i) const {
        return search_overlap(root, i);
    }
    inline bool empty() const {
        return root == nullptr;
    }
    inline void find_all_overlaped(Interval i, vector<Interval>& found) const {
        all_overlaped(root, i, found);
    }
};

// typedef double max_t;
typedef long long int max_t;

// pay == pby;
static inline bool testhh(
    int py, int minpx, int maxpx,
    int y, int x1, int x2) {
    
    return (y != py) || (x2 < minpx) || (x1 > maxpx);
}

// pay != pby;
static inline bool testh(
    int pax, int pay, int pbx, int pby,
    int minpx, int maxpx, int minpy, int maxpy,
    int y, int x1, int x2) {

    if (y < minpy || y > maxpy) {
        return true;
    }
    if (x1 > maxpx || x2 < minpx) {
        return true;
    }
    if (x1 <= minpx && x2 >= maxpx) {
        return false;
    }

    max_t dpx = pbx - pax;
    max_t dpy = pby - pay;
    max_t dy = y - pay;
    max_t dpx_dy = dpx*dy;
    if (dpx_dy >= max_t(x1-pax)*dpy && dpx_dy <= max_t(x2-pax)*dpy) {
        return false;
    }
    return true;
}


// pax == pbx
static inline bool testvv(
    int px, int minpy, int maxpy,
    int x, int y1, int y2) {
    
    return (x != px) || (y2 < minpy) || (y1 > maxpy);
}

// pax != pbx
static inline bool testv(
    int pax, int pay, int pbx, int pby,
    int minpx, int maxpx, int minpy, int maxpy,
    int x, int y1, int y2) {
    
    if (x < minpx || x > maxpx) {
        return true;
    }
    if (y1 > maxpy || y2 < minpy) {
        return true;
    }
    if (y1 <= minpy && y2 >= maxpy) {
        return false;
    }

    max_t dpx = pbx - pax;
    max_t dpy = pby - pay;
    max_t dx = x - pax;
    max_t dpy_dx = dpy*dx;
    if (dpy_dx >= max_t(y1-pay)*dpx && dpy_dx <= max_t(y2-pay)*dpx) {
        return false;
    }
    return true;
}

static inline bool check(
    tuple<int,int> pa,
    tuple<int,int> pb,
    const unordered_map<int, tuple<int, int, int, int> >& fences) {

    int pax, pay;
    int pbx, pby;
    pax = get<0>(pa);
    pay = get<1>(pa);
    pbx = get<0>(pb);
    pby = get<1>(pb);
    int minpx = min(pax, pbx);
    int maxpx = max(pax, pbx);
    int minpy = min(pay, pby);
    int maxpy = max(pay, pby);

    for (const auto& kv : fences) {
        auto t = kv.second;
        int x1, x2, y1, y2;
        x1 = get<0>(t);
        y1 = get<1>(t);
        x2 = get<2>(t);
        y2 = get<3>(t);
        // x1, y1, x2, y2 = f
        bool ok = true;
        if (pay == pby) {
            ok = true
                && testhh(pay, minpx, maxpx, y1, x1, x2) 
                && testhh(pay, minpx, maxpx, y2, x1, x2);            
        } else {
            ok = true
                && testh(pax, pay, pbx, pby, minpx, maxpx, minpy, maxpy, y1, x1, x2) 
                && testh(pax, pay, pbx, pby, minpx, maxpx, minpy, maxpy, y2, x1, x2);
        }
        if (!ok) {
            return false;
        }
        if (pax == pbx) {
            ok = true
                && testvv(pax, minpy, maxpy, x1, y1, y2) 
                && testvv(pax, minpy, maxpy, x2, y1, y2);
        } else {
            ok = true
                && testv(pax, pay, pbx, pby, minpx, maxpx, minpy, maxpy, x1, y1, y2) 
                && testv(pax, pay, pbx, pby, minpx, maxpx, minpy, maxpy, x2, y1, y2);
        }
        if (!ok) {
            return false;
        }
    }
    return true;
}



static inline bool check2(
    tuple<int,int> pa,
    tuple<int,int> pb,
    const map<int, map<int, int> >& hsegments,
    const map<int, map<int, int> >& vsegments) {
    
    int pax = get<0>(pa);
    int pay = get<1>(pa);
    int pbx = get<0>(pb);
    int pby = get<1>(pb);
    int minpx = min(pax, pbx);
    int maxpx = max(pax, pbx);
    int minpy = min(pay, pby);
    int maxpy = max(pay, pby);
    {
        auto hbeg = hsegments.lower_bound(minpy);
        auto hend = hsegments.upper_bound(maxpy);
        for (auto it = hbeg; it != hend; it++) {
            int y = it->first;
            auto& segs = it->second;
            //auto beg = segs.begin(); // lower_bound(minpx);
            //auto end = segs.upper_bound(maxpx);
            //for (auto itx = beg; itx != end; itx++) {
            for (const auto& kv : segs) {
                int x1 = kv.first;
                if (x1 > maxpx) {
                    break;
                }
                int x2 = kv.second;
                bool ok;
                if (pay == pby) {
                    ok = testhh(pay, minpx, maxpx, y, x1, x2);
                } else {
                    ok = testh(pax, pay, pbx, pby, minpx, maxpx, minpy, maxpy, y, x1, x2);
                }
                if (!ok) {
                    return false;
                }
            }    
        }
    }
    {
        auto vbeg = vsegments.lower_bound(minpx);
        auto vend = vsegments.upper_bound(maxpx);
        for (auto it = vbeg; it != vend; it++) {
            int x = it->first;
            auto& segs = it->second;
            //auto beg = segs.begin(); // lower_bound(minpy);
            //auto end = segs.upper_bound(maxpy);
            //for (auto ity = beg; ity != end; ity++) {
            for (const auto& kv : segs) {                
                int y1 = kv.first;
                if (y1 > maxpy) {
                    break;
                }
                int y2 = kv.second;
                bool ok;
                if (pax == pbx) {
                    ok = testvv(pax, minpy, maxpy, x, y1, y2);
                } else {
                    ok = testv(pax, pay, pbx, pby, minpx, maxpx, minpy, maxpy, x, y1, y2);
                }
                if (!ok) {
                    return false;
                }
            }    
        }
    }
    return true;
}


static inline bool check3(
    tuple<int,int> pa,
    tuple<int,int> pb,
    const map<int, itree>& hintervals,
    const map<int, itree>& vintervals) {
    
    int pax = get<0>(pa);
    int pay = get<1>(pa);
    int pbx = get<0>(pb);
    int pby = get<1>(pb);
    int minpx = min(pax, pbx);
    int maxpx = max(pax, pbx);
    int minpy = min(pay, pby);
    int maxpy = max(pay, pby);
    max_t dpx = pbx - pax;
    max_t dpy = pby - pay;
    if (pay == pby) {
        auto it = hintervals.find(pay);
        if (it != hintervals.end()) {
            int y = it->first;
            auto& segs = it->second;
            Interval interval(minpx, maxpx);
            vector<Interval> found;
            segs.find_all_overlaped(interval, found);
            for (const auto& i : found) {
                int x1 = i.low;
                int x2 = i.high;
                bool ok = testhh(pay, minpx, maxpx, y, x1, x2);
                if (!ok) {
                    return false;
                }
            }    
        }
    } else {
        auto hbeg = hintervals.lower_bound(minpy);
        auto hend = hintervals.upper_bound(maxpy);
        for (auto it = hbeg; it != hend; it++) {
            int y = it->first;
            auto& segs = it->second;
            int x = dpx * (y-pay) / dpy + pax;
            Interval interval(x, x+1);
            vector<Interval> found;
            segs.find_all_overlaped(interval, found);
            for (const auto& i : found) {
                int x1 = i.low;
                int x2 = i.high;
                bool ok = testh(pax, pay, pbx, pby, minpx, maxpx, minpy, maxpy, y, x1, x2);
                if (!ok) {
                    return false;
                }
            }    
        }
    }
    if (pax == pbx) {
        auto it = vintervals.find(pax);
        if (it != vintervals.end()) {
            int x = it->first;
            auto& segs = it->second;
            vector<Interval> found;
            Interval interval(minpy, maxpy);        
            segs.find_all_overlaped(interval, found);
            for (const auto& i : found) {
                int y1 = i.low;
                int y2 = i.high;
                bool ok = testvv(pax, minpy, maxpy, x, y1, y2);
                if (!ok) {
                    return false;
                }
            }    
        }
    } else {
        auto vbeg = vintervals.lower_bound(minpx);
        auto vend = vintervals.upper_bound(maxpx);
        for (auto it = vbeg; it != vend; it++) {
            int x = it->first;
            auto& segs = it->second;
            vector<Interval> found;
            int y = dpy * (x-pax) / dpx + pay;
            Interval interval(y, y+1);
            segs.find_all_overlaped(interval, found);
            for (const auto& i : found) {
                int y1 = i.low;
                int y2 = i.high;
                bool ok = testv(pax, pay, pbx, pby, minpx, maxpx, minpy, maxpy, x, y1, y2);
                if (!ok) {
                    return false;
                }
            }    
        }
    }
    return true;
}

int main() {
    unordered_map<int, tuple<int, int, int, int> > fences;
    // map<int, map<int, int> > hsegments;
    // map<int, map<int, int> > vsegments;
    map<int, itree> hintervals;
    map<int, itree> vintervals;
    int n, q;
    cin >> n >> q;
    vector<tuple<int,int> > p;
    p.reserve(n);
    for (int j = 0; j < n; j++) {
        int x, y;
        cin >> x >> y;
        p.push_back(make_tuple(x,y));
    }
    fences.reserve(q);
    for (int j = 0; j < q; j++) {
        string query;
        cin >> query;
        if (query == "add") {
            int x1, x2, y1, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            if (x1 > x2) {
                swap(x1, x2);
            }
            if (y1 > y2) {
                swap(y1, y2);
            }
            fences[j] = make_tuple(x1, y1, x2, y2);
            // hsegments[y1][x1] = x2;
            // hsegments[y2][x1] = x2;
            // vsegments[x1][y1] = y2;
            // vsegments[x2][y1] = y2;
            hintervals[y1].add(Interval(x1, x2));
            hintervals[y2].add(Interval(x1, x2));
            vintervals[x1].add(Interval(y1, y2));
            vintervals[x2].add(Interval(y1, y2));
        } else if (query == "delete") {
            int qid;
            cin >> qid;
            qid -= 1;
            auto f = fences[qid];
            int x1, x2, y1, y2;
            x1 = get<0>(f);
            y1 = get<1>(f);
            x2 = get<2>(f);
            y2 = get<3>(f);

            // hsegments[y1].erase(x1);
            // hsegments[y2].erase(x1);
            // vsegments[x1].erase(y1);
            // vsegments[x2].erase(y1);
            // if (hsegments[y1].size() == 0) {
            //     hsegments.erase(y1);
            // }
            // if (hsegments[y2].size() == 0) {
            //     hsegments.erase(y2);
            // }
            // if (vsegments[x1].size() == 0) {
            //     vsegments.erase(x1);
            // }
            // if (vsegments[x2].size() == 0) {
            //     vsegments.erase(x2);
            // }
            hintervals[y1].del(Interval(x1, x2));
            hintervals[y2].del(Interval(x1, x2));
            vintervals[x1].del(Interval(y1, y2));
            vintervals[x2].del(Interval(y1, y2));
            if (hintervals[y1].empty()) {
                hintervals.erase(y1);
            }
            if (hintervals[y2].empty()) {
                hintervals.erase(y2);
            }
            if (vintervals[x1].empty()) {
                vintervals.erase(x1);
            }
            if (vintervals[x2].empty()) {
                vintervals.erase(x2);
            }
            fences.erase(qid);
        } else if (query == "query") {
            int a, b;
            cin >> a >> b;
            // bool ok = check(p[a-1], p[b-1], fences);
            // bool ok = check2(p[a-1], p[b-1], hsegments, vsegments);
            bool ok = check3(p[a-1], p[b-1], hintervals, vintervals);
            cout << (ok ? "YES" : "NO") << endl;
        }
    }            
    return 0;
}
