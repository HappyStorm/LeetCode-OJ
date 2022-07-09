class MyQueue {
public:
    stack<int> stk1, stk2;
    int front = 0;
    MyQueue() {

    }

    void push(int x) {
        if(stk1.empty())
            front = x;
        stk1.push(x);
    }

    int pop() {
        if(stk2.empty())
            while(!stk1.empty()){
                stk2.push(stk1.top());
                stk1.pop();
            }
        int element = stk2.top();
        stk2.pop();
        return element;
    }

    int peek() {
        if(!stk2.empty())
            return stk2.top();
        return front;
    }

    bool empty() {
        return stk1.empty() && stk2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
