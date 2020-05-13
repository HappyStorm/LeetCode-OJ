class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"

        if not k:
            return num

        stk = []
        for n in num:
            while True:
                if not stk or not k:
                    break

                if stk[-1] > n:
                    stk.pop()
                    k -= 1

                else:
                    break

            stk += [n]

        while k:
            k -= 1
            stk.pop()

        i = 0
        while i < len(stk) and stk[i] == '0':
            i += 1

        return ''.join(stk[i:]) if i < len(stk) else '0'
