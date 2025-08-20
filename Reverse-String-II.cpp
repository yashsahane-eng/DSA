class Solution {
public:
    string reverseStr(string s, int k) {
        int n = s.size();
        int size = 2 * k;
        int temp = k;
        int i = 0;

        if(n < k || n == k){
            reverse(s.begin(), s.end());
            return s;
        }

        while(i < n){
            reverse(s.begin() + i, s.begin() + temp);
            i += size;
            temp += (2 * k);
            if(k == n) break;
            if((n - i) < (2 * k) && (n - i) >= k){
                reverse(s.begin() + i, s.begin() + temp);
                return s;
            }
            if(n - i < k){
                reverse(s.begin() +i, s.end());
                return s;
            }
        }
        return s;
    }
};