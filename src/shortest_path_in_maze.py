from collections import deque

def shortest_path_in_maze(maze, start, destination):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows, columns = len(maze), len(maze[0])
    visited = set()
    queue = deque([(start, 0)])  
    visited.add(start)

    while queue:
        (x, y), distance = queue.popleft()

        if (x, y) == destination:
            return distance

        for horizontal_move, vertical_move in directions:
            new_x, new_y = x + horizontal_move, y + vertical_move
            if 0 <= new_x < rows and 0 <= new_y < columns and maze[new_x][new_y] == 1 and (new_x, new_y) not in visited :
                visited.add((new_x,new_y))
                queue.append(((new_x, new_y), distance + 1))

    return None
