import re
from operator import mul
from functools import reduce

input_file = "06_input.txt"

with open(input_file) as f:
    raw = f.read().split("\n")

times = [int(item) for item in re.split('\s+', raw[0])[1:]]
dists = [int(item) for item in re.split('\s+', raw[1])[1:]]


def calc_num_wins(time, dist):
    win_dists = []
    
    for bpress in range(1,time):
        time_dist = (time-bpress)*bpress
        if time_dist > dist:
            win_dists.append(time_dist)

    return len(win_dists)

# part 1
num_wins = []

for i in range(0,len(times)):

    time = times[i]
    dist = dists[i]

    num_wins.append(calc_num_wins(time, dist))

print(reduce(mul, num_wins, 1))

# part 2
time = int(''.join(map(str, times)))
dist = int(''.join(map(str, dists)))

print(calc_num_wins(time, dist))
