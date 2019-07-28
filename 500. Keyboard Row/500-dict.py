class Solution(object):

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = {c: 0 for c in "qwertyuiopQWERTYUIOP"}
        rows.update({c: 1 for c in "asdfghjklASDFGHJKL"})
        rows.update({c: 2 for c in "zxcvbnmZXCVBNM"})
        return [word for word in words if all(map(lambda c: rows[c] == rows[word[0]], word))]
