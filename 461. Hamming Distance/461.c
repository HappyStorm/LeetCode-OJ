int hammingDistance(int x, int y) {
    int val = x^y;
    int ct = (val & 1);
    while (val>>=1)
        ct += (val & 1) ? 1 : 0;
    return ct;
}