class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_strs, v2_strs = version1.split('.'), version2.split('.')
        for i, (v1_str, v2_str) in enumerate(zip(v1_strs, v2_strs)):
            v1, v2 = int(v1_str), int(v2_str)
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            else:
                continue
        while i < len(v1_strs)-1:
            if int(v1_strs[i+1]):
                return 1
            else:
                i += 1
        while i < len(v2_strs)-1:
            if int(v2_strs[i+1]):
                return -1
            else:
                i += 1
        return 0
