class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        ans, n = [], len(code)
        if k > 0:
            for i in range(n):
                if i+k >= n:
                    ans.append(sum(code[i+1:] + code[:i+k-n+1]))
                else:
                    ans.append(sum(code[i+1:i+k+1]))
        else:
            for i in range(n):
                if i+k < 0:
                    ans.append(sum(code[:i] + code[i+k:]))
                else:
                    ans.append(sum(code[i+k:i]))
        return ans
