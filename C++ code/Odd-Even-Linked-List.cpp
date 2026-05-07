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
11 // BRUTE FORCE SOLUTION 
12class Solution {
13public:
14    ListNode* oddEvenList(ListNode* head) {
15        if(head==NULL || head->next==NULL){
16            return head;
17        }
18        vector<int>arr;
19        ListNode*temp=head;
20
21        while(temp !=NULL &&temp->next !=NULL){
22            arr.push_back(temp->val);
23            temp=temp->next->next;
24        }
25        if(temp !=NULL){
26            arr.push_back(temp->val);
27        }
28        temp=head->next;
29        while(temp !=NULL && temp->next != NULL){
30            arr.push_back(temp->val);
31            temp=temp->next->next;
32        }
33        if(temp!=NULL){
34            arr.push_back(temp->val);
35        }
36        int i=0;
37        temp=head;
38
39        while(temp!=NULL){
40            temp->val=arr[i];
41            i++;
42            temp=temp->next;
43        }
44        return head;
45        
46    }
47};