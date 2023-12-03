import re

input_file = "03_input.txt"


# determine symbols in input
with open(input_file) as f:
    alldata = f.read().replace("\n","")

symbols = set()
for item in alldata:
    if not item.isdigit() and not item=='.':
        symbols.add(item)

with open(input_file) as f:
    schematic = f.read().split("\n")
    
# part 1
summe = 0

for i, line in enumerate(schematic):
    ms = re.finditer("\d+", line)
    for m in ms:
        p1 = 0 if m.start()<=1 else m.start()-1
        p2 = m.end() if m.end()==len(line) else m.end()+1
        
        conds = []
        # line before
        if i>0:
            conds.append(any([symbol in schematic[i-1][p1:p2] for symbol in symbols]))
        # actual line
            conds.append(any([symbol in schematic[i][p1:p2] for symbol in symbols]))
        # next line
        if i<len(schematic)-1:
            conds.append(any([symbol in schematic[i+1][p1:p2] for symbol in symbols]))
                      
        if any(conds):
            summe += int(m.group())
            print(f"{m.group()} is schematic part!")

print(f"{summe=}")

# part 2

summe = 0
gear_candidates = []
gears = []

for i, line in enumerate(schematic):
    ms = re.finditer("\d+", line)
    for m in ms:
        p1 = 0 if m.start()<=1 else m.start()-1
        p2 = m.end() if m.end()==len(line) else m.end()+1
        
        conds = []
        # line before
        if i>0:
            for pos in range(p1, p2):
                if schematic[i-1][pos] == '*':
                    gear_candidates.append({"number": int(m.group()), "gear_i": i-1, "gear_pos": pos})
        # actual line
        for pos in range(p1, p2):
            if schematic[i][pos] == '*':
                gear_candidates.append({"number": int(m.group()), "gear_i": i, "gear_pos": pos})

        # next line
        if i<len(schematic)-1:
            for pos in range(p1, p2):
                if schematic[i+1][pos] == '*':
                    gear_candidates.append({"number": int(m.group()), "gear_i": i+1, "gear_pos": pos})
        
summe = 0
# now find gear_candidates which occur in two findings
for gear_candidate in gear_candidates:
    for gear_candidate_compare in gear_candidates:
        if gear_candidate is not gear_candidate_compare:
            if ((gear_candidate['gear_i'] == gear_candidate_compare['gear_i']) and
                (gear_candidate['gear_pos'] == gear_candidate_compare['gear_pos'])):
                summe += gear_candidate['number']*gear_candidate_compare['number']

summe /= 2

print(f"{summe=}")
