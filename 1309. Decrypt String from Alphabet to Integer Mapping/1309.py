class Solution:
    def freqAlphabets(self, s: str) -> str:
        num2alpha = {}
        for i in range(26):
            if i<9:
                num2alpha[str(i+1)] = chr(ord('a')+i)
            else:
                num2alpha[str(i+1)+'#'] = chr(ord('a')+i)

        ans, queue = [], []
        for i, c in enumerate(s):
            if c != '#':
                queue.append(c)
            else:
                second = queue.pop()
                first = queue.pop()
                ans += [num2alpha[qc] for qc in queue] +\
                       [num2alpha[first+second+'#']]
                queue.clear()
        ans += [num2alpha[qc] for qc in queue]
        return ''.join(ans)
