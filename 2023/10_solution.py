from operator import add

input_file = '10_input.txt'

with open(input_file) as f:
    raw = f.read().split("\n")
    
maze = [list(r) for r in raw]
    

directions = { ('west', '-'): (0,1,'west'), #'(dir_from, current pipe)': (delta_y, delta_x, dir_from_new)
               ('west', 'J'): (-1,0,'south'),
               ('west', '7'): (1,0,'north'),
               ('east', '-'): (0,-1,'east'),
               ('east', 'F'): (1,0,'north'),
               ('east', 'L'): (-1,0,'south'),
               ('north', '|'): (1,0,'north'),
               ('north', 'J'): (0,-1,'east'),
               ('north', 'L'): (0,1,'west'),
               ('south', '|'): (-1,0,'south'),
               ('south', '7'): (0,-1,'east'),
               ('south', 'F'): (0,1,'west'),
              }

term = False

# find S, initial position
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == 'S':
            pos = [y, x]
            print("S found")

# determine initial step, note: maze boundaries not considered, ok for this example
if maze[pos[0]-1][pos[1]] in ['|', '7', 'F']:
    origin = 'south'
    pos[0] -= 1
elif maze[pos[0]][pos[1]+1] in ['-', '7', 'J']:
    origin = 'west'
    pos[1] += 1
elif maze[pos[0]+1][pos[1]] in ['|', 'J', 'L']:
    origin = 'north'
    pos[0] += 1
elif maze[pos[0]][pos[1]-1] in ['-', 'L', 'F']:
    origin = 'east'
    pos[1] -= 1
else:
    print("should not happen")
#%%
steps = 1

while not term:
    current_pipe = maze[pos[0]][pos[1]]
    
    delta = directions[(origin, current_pipe)]
    
    pos[0] += delta[0]
    pos[1] += delta[1]
    origin = delta[2]
    
    steps += 1
    
    if maze[pos[0]][pos[1]] == 'S':
        print("terminal found")
        term = True

print(steps/2)        
# list(map(add, b, a))




# 7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ
