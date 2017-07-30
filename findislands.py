def numIslands(grid):
    if not grid:
        return 0

    row = len(grid)
    col = len(grid[0])

    seen = [[False for j in xrange(col)] for i in xrange(row)]

    count = 0
    queue = []

    for i in xrange(row):
        for j in xrange(col):
            if grid[i][j] == '1' and not seen[i][j]:

                count += 1
                queue.append(dfs(grid, seen, i, j, row, col, queue  ))
                print queue
                while len(queue) > 0:
                    queue[0]
                    queue = queue[1:]


    return count

def dfs(grid, seen, i, j, row, col, queue):
    if i >= row or j >= col or i < 0 or j < 0:
        return

    if grid[i][j] == '0' or seen[i][j]:
        return

    seen[i][j] = True
    print "i, j", i, j
    queue.append(dfs(grid, seen, i+1, j, row, col, queue))
    queue.append(dfs(grid, seen, i-1, j, row, col, queue))
    queue.append(dfs(grid, seen, i, j+1, row, col, queue))
    queue.append(dfs(grid, seen, i, j-1, row, col, queue))

    return;


island = [["1", "0", "1", "1"],
          ["1", "1", "0", "0"],
          ["1", "1", "0", "0"],
          ["1", "0", "0", "0"]]

print numIslands(island)
