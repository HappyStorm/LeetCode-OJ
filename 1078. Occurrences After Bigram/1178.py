class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_info = text.split(' ')

        ans = []
        for i in range(len(text_info)-1):
            if text_info[i] == first and text_info[i+1] == second:
                if i+2 < len(text_info):
                    ans += [text_info[i+2]]

                else:
                    ans += []

        return ans
