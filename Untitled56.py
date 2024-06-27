#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from collections import deque

def create_maze(size):
    maze = [['#' for _ in range(size)] for _ in range(size)]
    
    def carve_path(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + 2*dx, y + 2*dy
            if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] == '#':
                maze[x + dx][y + dy] = '.'
                maze[nx][ny] = '.'
                carve_path(nx, ny)
    
    maze[1][1] = '.'
    carve_path(1, 1)
    
    start = (1, 1)
    exit = (size - 2, size - 2)
    maze[start[0]][start[1]] = 'S'
    maze[exit[0]][exit[1]] = 'E'
    
    collectibles = []
    for _ in range(size // 2):
        while True:
            x, y = random.randint(1, size - 2), random.randint(1, size - 2)
            if maze[x][y] == '.':
                maze[x][y] = 'C'
                collectibles.append((x, y))
                break
    
    while True:
        ex, ey = random.randint(1, size - 2), random.randint(1, size - 2)
        if maze[ex][ey] == '.':
            enemy = (ex, ey)
            maze[ex][ey] = 'M'
            break
    
    return maze, start, exit, collectibles, enemy

def print_maze(maze):
    for row in maze:
        print(" ".join(row))
    print("\n")

def is_valid_move(maze, position):
    x, y = position
    size = len(maze)
    return 0 <= x < size and 0 <= y < size and maze[x][y] in ('.', 'E', 'C')

def find_path(maze, start, exit):
    queue = deque([start])
    visited = set()
    path = {start: None}
    
    while queue:
        current = queue.popleft()
        if current == exit:
            break
        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_pos = (current[0] + move[0], current[1] + move[1])
            if is_valid_move(maze, next_pos) and next_pos not in visited:
                queue.append(next_pos)
                visited.add(next_pos)
                path[next_pos] = current
    
    if exit not in path:
        return None
    
    reverse_path = []
    step = exit
    while step:
        reverse_path.append(step)
        step = path[step]
    
    return reverse_path[::-1]

def move_enemy(maze, enemy_pos):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(directions)
    for dx, dy in directions:
        new_pos = (enemy_pos[0] + dx, enemy_pos[1] + dy)
        if is_valid_move(maze, new_pos):
            return new_pos
    return enemy_pos

def maze_escape():
    size = 15
    maze, start, exit, collectibles, enemy_pos = create_maze(size)
    player_pos = start
    collected_items = 0
    
    print("Welcome to the Advanced Maze Escape Game with Collectibles and Enemy!")
    print_maze(maze)
    
    path = find_path(maze, start, exit)
    if not path:
        print("No valid path found in the maze!")
        return
    
    while player_pos != exit or collected_items < len(collectibles):
        move = input("Enter your move (up, down, left, right) or type 'hint' for a hint: ").lower()
        
        if move == 'up':
            new_pos = (player_pos[0] - 1, player_pos[1])
        elif move == 'down':
            new_pos = (player_pos[0] + 1, player_pos[1])
        elif move == 'left':
            new_pos = (player_pos[0], player_pos[1] - 1)
        elif move == 'right':
            new_pos = (player_pos[0], player_pos[1] + 1)
        elif move == 'hint':
            if len(path) > 1:
                hint = path[1]
                print(f"Hint: Move to position {hint}")
            else:
                print("You are already at the exit!")
            continue
        else:
            print("Invalid move. Please enter up, down, left, or right.")
            continue
        
        if is_valid_move(maze, new_pos):
            if maze[new_pos[0]][new_pos[1]] == 'C':
                collected_items += 1
                print(f"Collected an item! Total items collected: {collected_items}/{len(collectibles)}")
            maze[player_pos[0]][player_pos[1]] = '.'
            player_pos = new_pos
            maze[player_pos[0]][player_pos[1]] = 'P'
            path = find_path(maze, player_pos, exit)
            
            # Move the enemy
            maze[enemy_pos[0]][enemy_pos[1]] = '.'
            enemy_pos = move_enemy(maze, enemy_pos)
            maze[enemy_pos[0]][enemy_pos[1]] = 'M'
            
            print_maze(maze)
            
            if player_pos == enemy_pos:
                print("You were caught by the enemy! Game over.")
                return
        else:
            print("Invalid move. You hit a wall or went out of bounds.")
    
    print("Congratulations! You've collected all items and reached the exit to escape the maze!")

# Run the game
maze_escape()


# In[ ]:


import random
from collections import deque

def create_maze(size):
    maze = [['#' for _ in range(size)] for _ in range(size)]
    
    def carve_path(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + 2*dx, y + 2*dy
            if 0 <= nx < size and 0 <= ny < size and maze[nx][ny] == '#':
                maze[x + dx][y + dy] = '.'
                maze[nx][ny] = '.'
                carve_path(nx, ny)
    
    maze[1][1] = '.'
    carve_path(1, 1)
    
    start = (1, 1)
    exit = (size - 2, size - 2)
    maze[start[0]][start[1]] = 'S'
    maze[exit[0]][exit[1]] = 'E'
    
    collectibles = []
    for _ in range(size // 2):
        while True:
            x, y = random.randint(1, size - 2), random.randint(1, size - 2)
            if maze[x][y] == '.':
                maze[x][y] = 'C'
                collectibles.append((x, y))
                break
    
    while True:
        ex, ey = random.randint(1, size - 2), random.randint(1, size - 2)
        if maze[ex][ey] == '.':
            enemy = (ex, ey)
            maze[ex][ey] = 'M'
            break
    
    return maze, start, exit, collectibles, enemy

def print_maze(maze):
    for row in maze:
        print(" ".join(row))
    print("\n")

def is_valid_move(maze, position):
    x, y = position
    size = len(maze)
    return 0 <= x < size and 0 <= y < size and maze[x][y] in ('.', 'E', 'C')

def find_path(maze, start, exit):
    queue = deque([start])
    visited = set()
    path = {start: None}
    
    while queue:
        current = queue.popleft()
        if current == exit:
            break
        for move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_pos = (current[0] + move[0], current[1] + move[1])
            if is_valid_move(maze, next_pos) and next_pos not in visited:
                queue.append(next_pos)
                visited.add(next_pos)
                path[next_pos] = current
    
    if exit not in path:
        return None
    
    reverse_path = []
    step = exit
    while step:
        reverse_path.append(step)
        step = path[step]
    
    return reverse_path[::-1]

def move_enemy(maze, enemy_pos):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(directions)
    for dx, dy in directions:
        new_pos = (enemy_pos[0] + dx, enemy_pos[1] + dy)
        if is_valid_move(maze, new_pos):
            return new_pos
    return enemy_pos

def maze_escape():
    size = 15
    maze, start, exit, collectibles, enemy_pos = create_maze(size)
    player_pos = start
    collected_items = 0
    
    print("Welcome to the Advanced Maze Escape Game with Collectibles and Enemy!")
    print_maze(maze)
    
    path = find_path(maze, start, exit)
    if not path:
        print("No valid path found in the maze!")
        return
    
    while player_pos != exit or collected_items < len(collectibles):
        move = input("Enter your move (up, down, left, right) or type 'hint' for a hint: ").lower()
        
        if move == 'up':
            new_pos = (player_pos[0] - 1, player_pos[1])
        elif move == 'down':
            new_pos = (player_pos[0] + 1, player_pos[1])
        elif move == 'left':
            new_pos = (player_pos[0], player_pos[1] - 1)
        elif move == 'right':
            new_pos = (player_pos[0], player_pos[1] + 1)
        elif move == 'hint':
            if len(path) > 1:
                hint = path[1]
                print(f"Hint: Move to position {hint}")
            else:
                print("You are already at the exit!")
            continue
        else:
            print("Invalid move. Please enter up, down, left, or right.")
            continue
        
        if is_valid_move(maze, new_pos):
            if maze[new_pos[0]][new_pos[1]] == 'C':
                collected_items += 1
                print(f"Collected an item! Total items collected: {collected_items}/{len(collectibles)}")
            maze[player_pos[0]][player_pos[1]] = '.'
            player_pos = new_pos
            maze[player_pos[0]][player_pos[1]] = 'P'
            path = find_path(maze, player_pos, exit)
            
            # Move the enemy
            maze[enemy_pos[0]][enemy_pos[1]] = '.'
            enemy_pos = move_enemy(maze, enemy_pos)
            maze[enemy_pos[0]][enemy_pos[1]] = 'M'
            
            print_maze(maze)
            
            if player_pos == enemy_pos:
                print("You were caught by the enemy! Game over.")
                return
        else:
            print("Invalid move. You hit a wall or went out of bounds.")
    
    print("Congratulations! You've collected all items and reached the exit to escape the maze!")

# Run the game
maze_escape()


# In[ ]:




