
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        vector<vector<int>> len;
        len.resize(matrix.size());
        for (int i = 0; i < matrix.size(); i++) {
            len[i].resize(matrix[i].size());
            for (int &l : len[i]) {
                l = 0;
            }
        }
        int longestL = 0;
        for (int y = 0; y < matrix.size(); y++) {
            for (int x = 0; x < matrix[y].size(); x++) {
                int l = longest(matrix, x, y, len);
                if (l > longestL) {
                    longestL = l;
                } 
            }
        }
        return longestL;
    }
    
    int longest(vector<vector<int>>& matrix, int x, int y, vector<vector<int>>& len) {
        int dx[] = {0, 0, 1, -1};
        int dy[] = {-1, 1, 0, 0};
        
        int l = len[y][x];
        if (l > 0) {
            return l;
        }

        int v = matrix[y][x];
        
        l = 1;
        for (int k = 0; k < 4; k++) {
            int x1 = x + dx[k];
            int y1 = y + dy[k];
            if (x1 >= 0 && y1 >= 0 && y1 < matrix.size() && x1 < matrix[y1].size()) {
                int v1 = matrix[y1][x1];
                if (v1 < v) {
                    int l1 = longest(matrix, x1, y1, len) + 1;
                    if (l1 > l) {
                        l = l1;
                    }
                }
            }
        }
        len[y][x] = l;
        return l;
    }
};

