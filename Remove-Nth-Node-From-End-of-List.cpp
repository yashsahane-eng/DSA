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
13    ListNode* removeNthFromEnd(ListNode* head, int n) {
14        if(head==NULL){
15            return NULL;
16        }
17        int cnt=0;
18        ListNode*temp=head;
19
20        while(temp !=NULL){
21            cnt++;
22            temp=temp->next;
23
24        }
25        if(cnt==n){
26            ListNode*newHead=head->next;
27            delete(head);
28            return newHead;
29        }
30        int res=cnt-n;
31        temp=head;
32
33        while(temp !=NULL){
34            res--;
35            if(res==0){
36                break;
37            }
38            temp=temp->next;
39        }
40        ListNode*delNode=temp->next;
41        temp->next=temp->next->next;
42        delete(delNode);
43        return head;
44
45
46    }
47};