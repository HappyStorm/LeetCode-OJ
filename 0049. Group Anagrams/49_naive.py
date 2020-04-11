class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if str_dict.get(sorted_s):
                str_dict[sorted_s] += [s]

            else:
                str_dict[sorted_s] = [s]

        return str_dict.values()