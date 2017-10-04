

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



int main() {
    int p;
    cin >> p;
    for (int k = 0; k < p; k++) {
        int r, c, n, m;
        cin >> r >> c >> n >> m;
        vector<itree> plantations;
        plantations.resize(r);
        for (int i = 0; i < n; i++) {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            Interval intrv(x1, x2);
            for (int y = y1; y <= y2; y++) {
                plantations[y].add(intrv);
                cout << "add " << y << ": " << "[" << intrv.low << ";" << intrv.high << "]" << endl;

            }
        }
        vector<vector<int> > grid;
        grid.resize(r);
        for (int i = 0; i < r; i++) {
            grid[i].resize(c);
            itree& tree = plantations[i];
            for (int j = 0; j < c; j++) {
                Interval point(j, j);
                vector<Interval> found;
                tree.find_all_overlaped(point, found);
                grid[i][j] = found.size();
                cout << i << "," << j << ": ";
                for (auto ix : found) {
                    cout << "[" << ix.low << ";" << ix.high << "],";
                }
                cout << endl;
            }
        }
        for (int i = 0; i < r; i++) {
            for (auto w : grid[i]) {
                cout << w << " ";
            }
            cout << endl;
        }
    }
    return 0;
}
