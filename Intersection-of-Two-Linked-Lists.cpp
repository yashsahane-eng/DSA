1/**
2 * Definition for singly-linked list.
3 * struct ListNode {
4 *     int val;
5 *     ListNode *next;
6 *     ListNode(int x) : val(x), next(NULL) {}
7 * };
8 */
9class Solution {
10public:
11    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
12        unordered_set<ListNode*>nodes_set;
13
14        while(headA !=NULL){
15            nodes_set.insert(headA);
16            headA=headA->next;
17
18        }
19        while(headB !=NULL){
20            if(nodes_set.find(headB)!=nodes_set.end()){
21                return headB;
22            }
23            headB=headB->next;
24        }
25        return NULL;
26        
27    }
28};