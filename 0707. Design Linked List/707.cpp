struct Node {
    int val;
    Node *next;
    Node(int x): val(x), next(nullptr) {}
};

class MyLinkedList {
    int len;
    Node *head;
    public:
        MyLinkedList() {
            head = new Node(0);
            len = 0;
        }

        int get(int index) {
            if(index>=len) return -1;
            Node *cur = head;
            for (int i=0; i<index; ++i) cur = cur->next;
            return cur->next->val;
        }

        void addAtHead(int val) {
            Node *cur = new Node(val);
            cur->next = head->next;
            head->next = cur;
            len++;
        }

        void addAtTail(int val) {
            Node *cur = head;
            for (int i=0; i<len; ++i) cur = cur->next;
            Node *tmp = new Node(val);
            cur->next = tmp;
            len++;
        }

        void addAtIndex(int index, int val) {
            if (index > len) return;
            Node *cur = head;
            for (int i=0; i<index; ++i) cur = cur->next;
            Node *tmp = new Node(val);
            tmp->next = cur->next;
            cur->next = tmp;
            len++;
        }

        void deleteAtIndex(int index) {
            if (index >= len) return;
            Node *cur = head;
            for (int i=0; i<index; ++i) cur = cur->next;
            Node *del = cur->next;
            cur->next = cur->next->next;
            del->next = nullptr;
            delete del;
            len--;
        }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
