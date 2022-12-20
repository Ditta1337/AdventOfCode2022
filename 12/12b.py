from collections import deque

with open("/Users/ditta/Desktop/AGH/AdventOfCode2022/12/input.txt") as f:
    data = f.readlines()


grid = [list(row.strip()) for row in data]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
width = len(grid[0])
height = len(grid)


def findEnd(start=0, end=0):

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "E":
                end = (i, j)
    
    grid[end[0]][end[1]] = "z"

    return end


def BFS():
    end = findEnd()
    queue = deque()
    visited = set()

    queue.append((end, 0))
    visited.add(end)

    while queue:
        pos, depth = queue.popleft()
        if grid[pos[0]][pos[1]] == "a":
            print(grid[pos[0]][pos[1]])
            return depth
        for d in directions:
            next_pos = (pos[0] + d[0], pos[1] + d[1])
            if (
                0 <= next_pos[0] < height
                and 0 <= next_pos[1] < width
                and next_pos not in visited
            ):
                if ord(grid[next_pos[0]][next_pos[1]]) >= ord(grid[pos[0]][pos[1]]) - 1:
                    queue.append((next_pos, depth + 1))
                    visited.add(next_pos)

print(BFS())

f.close()
