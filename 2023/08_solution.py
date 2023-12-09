import re


def load(input_file):

    with open(input_file) as f:
        raw = f.read().split("\n")
    
    
    commands = [c for c in raw[0]]
    
    directions = { re.findall('[A-Z0-9]{3}', r)[0]:
                  (re.findall('[A-Z0-9]{3}', r)[1],
                   re.findall('[A-Z0-9]{3}', r)[2]) for r in raw[2:]}
        
    return (commands, directions)
    
# part 1

def part1(input_file):
    cmds, dirs = load(input_file)
    p = 'AAA'
    i = 0
    while not p == 'ZZZ':
        cmd = cmds[i % len(cmds)]
        p = dirs[p][0] if cmd=='L' else dirs[p][1]
        i += 1
    
    print(f'{i=}')
        
# part 2

def part2(input_file):
    cmds, dirs = load(input_file)
    ps = [ key for key in list(dirs.keys()) if key[2]=='A' ] # positions
    i = 0
    while not all([p[2]=='Z' for p in ps]):
        cmd = cmds[i % len(cmds)]
        ps = [dirs[p][0] if cmd=='L' else dirs[p][1] for p in ps]
        i += 1
    
    print(f'{i=}')        

# main

part1('08_test_part1.txt')
part1('08_input.txt')

part2('08_test_part1.txt')
#part2('08_input.txt')  --> does not work with brute force method


#%% part2, ernsthaft

cmds, dirs = load("08_input.txt")
ps = [ key for key in list(dirs.keys()) if key[2]=='A' ] # positions
i = 0


i_where_z = []
for _ in ps:
    i_where_z.append([])
    

while not all([len(a)>4 for a in i_where_z]):
    cmd = cmds[i % len(cmds)]
    ps = [dirs[p][0] if cmd=='L' else dirs[p][1] for p in ps]
    for j, p_ in enumerate(ps):
        if p_[2]=='Z':
            i_where_z[j].append(i)
    i += 1
    
import numpy as np
for aa in i_where_z:
    print(np.diff(np.array(aa)))

# [a[i+1]-a[i] for i in range(len(a)-1)]
    
# [11653 11653 11653 11653 11653 11653 11653]
# [19783 19783 19783 19783]
# [19241 19241 19241 19241]
# [16531 16531 16531 16531]
# [12737 12737 12737 12737 12737 12737]
# [14363 14363 14363 14363 14363]    
# --> Periodizitäten treten auf, kleinestes gemeinsames Vielfaches finden
# https://stackoverflow.com/questions/15347174/python-finding-prime-factors

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

prime_factors(11653)
prime_factors(19783)
prime_factors(19241)
prime_factors(16531)
prime_factors(12737)
prime_factors(14363)
43*271*73*71*61*47*53
