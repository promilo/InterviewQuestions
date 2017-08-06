def numIslands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rowlen = len(grid)
        collen = len(grid[0])
        visited = [[False for x in range(collen)] for x in range(rowlen)]

        count = 0
        for x in range(rowlen):
            for y in range(collen):
                if grid[x][y] == '1' and not visited[x][y]:
                    count += 1
                    dfs(grid, visited, rowlen, collen, x, y)

        return count

    def dfs(grid, visited, rowlen, collen, x, y):
        if grid[x][y] == '0' or visited[x][y] or x >= rowlen or y >= collen or x < 0 or y < 0:
            return
        visited[x][y] = True

        dfs(grid, visited, rowlen, collen, x + 1, y)
        dfs(grid, visited, rowlen, collen, x - 1, y)
        dfs(grid, visited, rowlen, collen, x, y + 1)
        dfs(grid, visited, rowlen, collen, x, y - 1)
