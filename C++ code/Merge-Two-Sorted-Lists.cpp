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
11
12 // OPTIMAL SOLUTION
13class Solution {
14public:
15    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
16        ListNode*dummyNode=new ListNode(-1);
17        ListNode* temp=dummyNode;
18
19        while(list1 !=nullptr && list2 !=nullptr){
20            if(list1->val <= list2->val){
21                temp->next=list1;
22                list1=list1->next;
23            }else{
24                temp->next=list2;
25                list2=list2->next;
26            }
27            temp=temp->next;
28        }
29        if(list1 !=nullptr){
30            temp->next=list1;
31        }else{
32            temp->next=list2;
33        }
34        return dummyNode->next;
35        
36    }
37};