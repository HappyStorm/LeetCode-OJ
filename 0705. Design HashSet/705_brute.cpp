class MyHashSet {
public:
    vector<bool> dict;
    MyHashSet() {
        dict.resize(1e6+1, false);
    }

    void add(int key) {
        dict[key] = true;
    }

    void remove(int key) {
        dict[key] = false;
    }

    bool contains(int key) {
        return dict[key];
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
