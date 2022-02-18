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
            if n != '0' or stk:
                stk += [n]

        while k and stk:
            k -= 1
            stk.pop()

        return ''.join(stk) if stk else '0'
