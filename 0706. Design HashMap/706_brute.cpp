class MyHashMap {
public:
    vector<int> dict;
    MyHashMap() {
        dict.resize(1e6+1, -1);
    }

    void put(int key, int value) {
        dict[key] = value;
    }

    int get(int key) {
        if(dict[key]!=-1)
            return dict[key];
        else
            return -1;
    }

    void remove(int key) {
        dict[key] = -1;
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */