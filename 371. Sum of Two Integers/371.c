int getSum(int a, int b) {
    char *c = (char *) a;
    return (int) &c[b];
}