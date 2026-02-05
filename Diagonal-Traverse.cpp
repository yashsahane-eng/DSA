1class Solution {
2public:
3    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
4        if (matrix.empty() || matrix[0].empty()) return {};
5
6        int m = matrix.size(), n = matrix[0].size();
7        vector<int> result(m * n);
8        int row = 0, col = 0;
9
10        for (int i = 0; i < m * n; i++) {
11            result[i] = matrix[row][col];
12
13            if ((row + col) % 2 == 0) {
14                if (col == n - 1) row++;
15                else if (row == 0) col++;
16                else { row--; col++; }
17            } else {
18                if (row == m - 1) col++;
19                else if (col == 0) row++;
20                else { row++; col--; }
21            }
22        }
23
24        return result;
25    }
26};