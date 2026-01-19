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
11 // ITERATIVE SOLUTION 
12class Solution {
13public:
14    ListNode* reverseList(ListNode* head) {
15        ListNode*temp=head;
16        ListNode*prev=NULL;
17
18        while(temp !=NULL){
19            ListNode*front=temp->next;
20            temp->next=prev;
21            prev=temp;
22            temp=front;
23        }
24        return prev;
25        
26    }
27};