

struct ListNode{
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr){}
    ListNode(int _val) : val(_val), next(nullptr){}
    ListNode(int _val, ListNode* _next) : val(_val), next(_next){}
};

class Solution{
public:
    ListNode* sortList(ListNode* head){
        // 如果链表的节点数是 0 或 1
        if(head == nullptr || head->next == nullptr)
            return head;

        ListNode *temp = nullptr;
        ListNode *slow = head;
        ListNode *fast = head;

        while(fast != nullptr && fast->next != nullptr){
            temp = slow;
            // 慢指针进 1 步
            slow = slow->next;
            // 快指针进 2 步
            fast = fast->next->next;
        }
        // 左半边的末尾
        temp->next = nullptr;

    }
};



int main(int argc, char** argv){
    // ListNode n1, n2, n3, n4;
    // n1.val = 4; n1.next = &n2;
    // n1.val = 2; n1.next = &n3;
    // n1.val = 1; n1.next = &n4;
    // n1.val = 3;
    // Solution s;
    // s.sortList(&n1);

    return 0;
}