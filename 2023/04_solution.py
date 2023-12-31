input_file = "04_input.txt"


with open(input_file) as f:
    cards = f.read().split("\n")


# part 1
sum_deck = 0

for card in cards:
    winning_numbers = [int(item) for item in card.split('|')[0].split(':')[1].split()]
    my_numbers = [int(item) for item in card.split('|')[1].split()]
    
    sum_card = 0
    for my_number in my_numbers:
        for winning_number in winning_numbers:
            if my_number == winning_number:
                sum_card += 1
    
    if sum_card > 0:
        sum_deck += 2**(sum_card-1)
        
print(sum_deck)
        
# part 2

counters = [1]*len(cards)

for i, card in enumerate(cards):
    winning_numbers = [int(item) for item in card.split('|')[0].split(':')[1].split()]
    my_numbers = [int(item) for item in card.split('|')[1].split()]

    sum_card = 0
    for my_number in my_numbers:
        for winning_number in winning_numbers:
            if my_number == winning_number:
                sum_card += 1

    if sum_card > 0:
        for j in range(i+1, i+sum_card+1):
            if j < len(counters):
                counters[j] += counters[i]

print(sum(counters))