def load(input_file):

    with open(input_file) as f:
        raw = f.read().split("\n")
    
    sequences = [[int(s) for s in r.split(' ')] for r in raw]
        
    return sequences


def part1(input_file):
    seqs = load(input_file)

    for seq in seqs:
        exa = [seq]
        depth = 0
        
        while not all([n==0 for n in exa[depth]]):
            exa.append([exa[depth][i+1]-exa[depth][i] for i in range(len(exa[depth])-1)])
            depth += 1
        
        for i in range(len(exa)-2, 0, -1):
            exa[i-1].append(exa[i-1][-1] + exa[i][-1])
    
    the_sum = sum([seq[-1] for seq in seqs])
    print(f'{the_sum=}')


def part2(input_file):
    seqs = load(input_file)
    
    for seq in seqs:
        exa = [seq]
        depth = 0
        
        while not all([n==0 for n in exa[depth]]):
            exa.append([exa[depth][i+1]-exa[depth][i] for i in range(len(exa[depth])-1)])
            depth += 1
        
        for i in range(len(exa)-2, 0, -1):
            exa[i-1].insert(0, exa[i-1][0] - exa[i][0])
    
    the_sum = sum([seq[0] for seq in seqs])
    print(f'{the_sum=}')


part1('09_test.txt')    
part1('09_input.txt')

part2('09_test.txt')    
part2('09_input.txt')

