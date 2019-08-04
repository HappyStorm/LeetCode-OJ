class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_info = text.split(' ')

        ans = []
        for i in range(len(text_info) - 2):
            if text_info[i] == first and text_info[i + 1] == second:
                ans += [text_info[i + 2]]

        return ans
