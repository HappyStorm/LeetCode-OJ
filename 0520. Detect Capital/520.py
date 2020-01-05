class Solution(object):

    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return not not list(filter(re.compile("([A-Z]*|[A-Z{1}][a-z]*|[a-z]*)$").match, [word]))
