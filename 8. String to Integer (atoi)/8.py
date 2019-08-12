class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        word = str.strip().split(' ')[0]

        if len(word) == 0:
            return 0

        if word[0].isalpha():
            return 0

        sign = 1
        if word[0] == '-' or word[0] == '+':
            sign = -1 if word[0] == '-' else 1
            word = word[1:]

        nums = []
        for c in word:
            if c.isdigit():
                nums += [int(c)]

            else:
                break

        ans = 0
        for i, n in enumerate(nums[::-1]):
            ans += n * (10**i)

        ans *= sign
        if ans > INT_MAX:
            return INT_MAX

        if ans < INT_MIN:
            return INT_MIN

        return ans