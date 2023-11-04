class Maze:
    def __init__(self, n):
        self.n = n
        self.maze = [['█' for i in range(2 * n + 1)] for j in range(2 * n + 1)]
        for i in range(n):
            for j in range(n):
               self.maze[2 * i + 1][2 * j + 1] = '·'

    def __setitem__(self, coords, value):
        y0, x0 = coords[0], coords[1].start
        y1, x1 = coords[1].stop, coords[2]
        if x0 == x1:
            for j in range(2 * min(y0, y1) + 1, 2 * max(y0, y1) + 2):
                if (j + x0 * 2 + 1) % 2:
                    self.maze[x0 * 2 + 1][j] = value
        if y0 == y1:
            for i in range(2 * min(x0, x1) + 1, 2 * max(x0, x1) + 2):
                if (i + y0 * 2 + 1) % 2:
                    self.maze[i][y0 * 2 + 1] = value        
    
    def __getitem__(self, coords):
        y0, x0 = coords[0] * 2 + 1, coords[1].start * 2 + 1
        y1, x1 = coords[1].stop * 2 + 1, coords[2] * 2 + 1
        seen = set()
        plan = []
        plan.append((x0, y0))
        while plan:
            x, y = plan.pop()
            seen.add((x, y))
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if self.maze[x + i][y + j] == '·' and (x + i, y + j) not in seen:
                        plan.append((x + i, y + j))
        if (x1, y1) in seen:
            return True
        return False

    def __str__(self):
        out = []
        for i in self.maze:
            for j in i:
                out.append(j)
            out.append('\n')
        return ''.join(out[:-1])

import sys
exec(sys.stdin.read())
