char findTheDifference(char* s, char* t) {
    int i=0, j=1;
    while (s[i]!='\0') t[0] ^= s[i++];
    while (t[j]!='\0') t[0] ^= t[j++];
    return t[0];
}