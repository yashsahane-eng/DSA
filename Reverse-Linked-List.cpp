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
11 // RECURSIVE SOLUTION
12class Solution {
13public:
14    ListNode* reverseList(ListNode* head) {
15        if(head==NULL || head->next==NULL){
16            return head;
17        }
18        ListNode*newHead=reverseList(head->next);
19        ListNode*front=head->next;
20        front->next=head;
21        head->next=NULL;
22        return newHead;
23        
24    }
25};