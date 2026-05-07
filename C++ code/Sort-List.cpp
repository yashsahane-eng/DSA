1/**
2 * Definition for singly-linked list.
3 * struct ListNode {
4 *     int val;
5 *     ListNode *next;
6 *     ListNode() : val(0), next(nullptr) {}
7 *     ListNode(int x) : val(x), next(nullptr) {}
8 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
9 * };
10 */ // BRUTE FORCE SOLUTION
11class Solution {
12public:
13    ListNode* sortList(ListNode* head) {
14        vector<int>arr;
15        ListNode*temp=head;
16
17        while(temp !=NULL){
18            arr.push_back(temp->val);
19            temp=temp->next;
20        }
21        sort(arr.begin(),arr.end());
22        temp=head;
23
24        for(int i=0;i<arr.size();i++){
25            temp->val=arr[i];
26            temp=temp->next;
27        }
28        return head;
29        
30    }
31};