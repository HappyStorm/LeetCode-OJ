class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        occurence = set()
        for v in counter.values():
            if v in occurence:
                return False
            occurence.add(v)
        return True
