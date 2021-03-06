class Solution(object):

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [set("qwertyuiopQWERTYUIOP"),
                set("asdfghjklASDFGHJKL"),
                set("zxcvbnmZXCVBNM")]
        return [word for word in words for row in rows if len(set(word) - row) == 0]
