1class Solution {
2public:
3    int bitwiseComplement(int n) {
4        if (n == 0)
5            return 1;
6
7        int temp = n;
8        int mask = 0;
9
10        while (temp > 0) {
11            mask = (mask << 1) | 1;
12            temp >>= 1;
13        }
14        return n ^ mask;
15    }
16};