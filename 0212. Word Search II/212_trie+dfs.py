class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}

            cur = cur[c]

        cur['is_word'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur:
                return False

            cur = cur[c]

        return cur.get('is_word', False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for c in prefix:
            if c not in cur:
                return False

            cur = cur[c]

        return True

class Solution:
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(self, cur, board, r, c, route, ans):
        if cur.get('is_word'):
            ans.append(route)
            cur['is_word'] = False

        if not(0 <= r < len(board)) or not(0 <= c < len(board[0])):
            return

        char = board[r][c]
        cur = cur.get(char)
        if not cur:
            return

        board[r][c] = '*'
        for mr, mc in self.moves:
            self.dfs(cur, board, r+mr, c+mc, route+char, ans)
        board[r][c] = char

        return


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        trie = Trie()
        cur = trie.root
        for word in words:
            trie.insert(word)

        row, col = len(board), len(board[0])
        for r in range(row):
            for c in range(col):
                self.dfs(cur, board, r, c, '', ans)

        return ans
