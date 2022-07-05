/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        set<ListNode*> hist;
        set<ListNode*>::iterator iter;
        ListNode *cur = head;
        while(cur!=NULL){
            iter = hist.find(cur);
            if(iter!=hist.end())
                return cur;
            else
                hist.insert(cur);
            cur = cur->next;
        }
        return NULL;
    }
};
