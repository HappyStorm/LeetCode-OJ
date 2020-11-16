class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        ans, n, code = [], len(code), code*2
        if k > 0:
            for i in range(n):
                ans.append(sum(code[i+1:i+k+1]))
        else:
            for i in range(n):
                ans.append(sum(code[i+n+k:i+n]))
        return ans
