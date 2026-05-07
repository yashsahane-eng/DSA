1/**
2 * Definition for singly-linked list.
3 * struct ListNode {
4 *     int val;
5 *     ListNode *next;
6 *     ListNode() : val(0), next(nullptr) {}
7 *     ListNode(int x) : val(x), next(nullptr) {}
8 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
9 * };
10 */
11class Solution {
12public:
13    bool isPalindrome(ListNode* head) {
14        stack<int>st;
15
16        ListNode*temp=head;
17        
18        while(temp != NULL){
19            st.push(temp->val);
20            temp=temp->next;
21        }
22        temp=head;
23        while(temp !=NULL){
24            if(temp->val != st.top()){
25                return false;
26            }
27            st.pop();
28            temp=temp->next;
29        }
30        return true;
31
32        
33    }
34};