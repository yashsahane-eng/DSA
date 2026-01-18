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
13    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
14        vector<int>arr;
15        ListNode* temp1=list1;
16        ListNode* temp2=list2;
17
18        while(temp1 !=NULL){
19            arr.push_back(temp1->val);
20            temp1=temp1->next;
21        }
22        while(temp2 !=NULL){
23            arr.push_back(temp2->val);
24            temp2=temp2->next;
25        }
26
27        sort(arr.begin(),arr.end());
28
29        ListNode*dummyNode=new ListNode(-1);
30        ListNode*temp=dummyNode;
31        for(int i=0;i<arr.size();i++){
32            temp->next=new ListNode(arr[i]);
33            temp=temp->next;
34        }
35        return dummyNode->next;
36
37        
38    }
39};