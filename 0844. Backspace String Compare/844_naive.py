class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_que, t_que = [], []
        for c in S:
            if c != '#':
                s_que += [c]

            else:
                if s_que:
                    s_que.pop()

        for c in T:
            if c != '#':
                t_que += [c]

            else:
                if t_que:
                    t_que.pop()

        return s_que == t_que