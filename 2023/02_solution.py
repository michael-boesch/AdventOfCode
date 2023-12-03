# parse input

with open('02_input.txt') as f:
    games_str = f.read().split("\n")
    
games = dict()

for game in games_str:
    game_id = int(game.split(':')[0].split()[1])

    moves = game.split(':')[1].split(';')

    max_col={"red": 0, "green": 0, "blue": 0}
    for move in moves:
        items = move.split(',')    

        for item in items:
            max_col[item.strip().split(' ')[1]] = max(max_col[item.strip().split(' ')[1]],
                                                      int(item.strip().split(' ')[0]))
    games[game_id] = max_col


# evaluate part 1

requirement = {"red": 12, "green": 13, "blue": 14}

sum_feasible_game_ids = 0

for game_id in games:
    if (games[game_id]["red"] <= requirement["red"] and
        games[game_id]["green"] <= requirement["green"] and
        games[game_id]["blue"] <= requirement["blue"]):
        sum_feasible_game_ids += game_id
        
# evaluate part 2

sum_power = 0

for game_id in games:
    sum_power += (games[game_id]["red"]*
                  games[game_id]["green"]*
                  games[game_id]["blue"])