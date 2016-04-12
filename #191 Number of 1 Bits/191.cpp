class Solution {
public:
    int hammingWeight(uint32_t n) {
        // method 1: by C++ STL library <Bitset>
        std::bitset<32> bit(n);
        return bit.count();
        
        // method 2: by GCC built-in function
        // return __builtin_popcount(n);
    }
};