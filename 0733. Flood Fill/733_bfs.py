class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visit, queue = [[0]*col for _ in range(row)], [(sr, sc)]
        initColor = image[sr][sc]
        while queue:
            r, c = queue.pop()
            if (0 <= r < row and 0 <= c < col) and image[r][c] == initColor and not visit[r][c]:
                visit[r][c] = 1
                image[r][c] = newColor
                for m in move:
                    tr, tc = r + m[0], c + m[1]
                    queue = [(tr, tc)] + queue

        return image
