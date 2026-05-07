1/**
2 * Definition for singly-linked list.
3 * struct ListNode {
4 *     int val;
5 *     ListNode *next;
6 *     ListNode() : val(0), next(nullptr) {}
7 *     ListNode(int x) : val(x), next(nullptr) {}
8 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
9 * };
10 */ //OPTIMAL SOLUTION
11class Solution {
12public:
13    ListNode* removeNthFromEnd(ListNode* head, int n) {
14        ListNode*fast=head;
15        ListNode*slow=head;
16
17        for(int i=0 ;i<n;i++){
18            fast=fast->next;
19        }
20        if(fast ==NULL){
21            return head->next;
22        }
23        while(fast->next != NULL){
24            slow=slow->next;
25            fast=fast->next;
26        }
27        ListNode*delNode=slow->next;
28        slow->next=slow->next->next;
29        delete(delNode);
30        return head;
31
32
33        
34    }
35};