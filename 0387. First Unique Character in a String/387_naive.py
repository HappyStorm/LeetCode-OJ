class Solution:
    def firstUniqChar(self, s: str) -> int:
        lset = set()
        ans_list, ans_dict = [], {}
        for i, c in enumerate(s):
            if c not in lset:
                lset.add(c)
                ans_list += [i]
                ans_dict[c] = i

            else:
                if ans_dict.get(c) is not None:
                    ans_list.remove(ans_dict[c])
                    del ans_dict[c]

        return ans_list[0] if ans_list else -1
