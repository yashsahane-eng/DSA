1class Solution {
2public:
3    int findComplement(int num) {
4
5        if (num == 0)
6            return 1;
7
8        int temp = num;
9        int mask = 0;
10
11        while (temp > 0) {
12            mask = (mask << 1) | 1;
13            temp >>= 1;
14        }
15        return num ^ mask;
16    }
17};