input_file = "07_input.txt"

with open(input_file) as f:
    raw = f.read().split("\n")

deck = [{"hand": item.split(' ')[0], "bid": int(item.split(' ')[1])} for item in raw]
    

#%%
card_ranks = {'A': 13,
              'K': 12,
              'Q': 11,
              'J': 10,
              'T': 9,
              '9': 8,
              '8': 7,
              '7': 6,
              '6': 5,
              '5': 4,
              '4': 3,
              '3': 2,
              '2': 1}

hand_ranks = {'five_of_a_kind': 7,
              'four_of_a_kind': 6,
              'full_house': 5,
              'three_of_a_kind': 4,
              'two_pairs': 3,
              'one_pair': 2,
              'high_card': 1}

def determine_hand_rank(hand):
    chars = [c for c in hand]
    freq = {char:chars.count(char) for char in set(chars)}
    
    if max(freq.values()) == 5:
        hand_rank = 'five_of_a_kind'
    elif max(freq.values()) == 4:
        hand_rank = 'four_of_a_kind'
    elif sorted(list(freq.values()), reverse=True) == [3,2]:
        hand_rank = 'full_house'
    elif max(freq.values()) == 3:
        hand_rank = 'three_of_a_kind'
    elif sorted(list(freq.values()), reverse=True) == [2,2,1]:
        hand_rank = 'two_pairs'
    elif max(freq.values()) == 2:
        hand_rank = 'one_pair'
    else:
        hand_rank = 'high_card'

    return hand_rank    


def determine_max_possible_with_joker(hand):
    
    
    pass



def is_first_hand_higher_than_second_hand(hand1, hand2):
    if hand_ranks[determine_hand_rank(hand1)] > hand_ranks[determine_hand_rank(hand2)]:
        return True
    elif hand_ranks[determine_hand_rank(hand1)] == hand_ranks[determine_hand_rank(hand2)]:
        if card_ranks[hand1[0]] > card_ranks[hand2[0]]:
            return True
        elif card_ranks[hand1[0]] == card_ranks[hand2[0]]:
            if card_ranks[hand1[1]] > card_ranks[hand2[1]]:
                return True
            elif card_ranks[hand1[1]] == card_ranks[hand2[1]]:
                if card_ranks[hand1[2]] > card_ranks[hand2[2]]:
                    return True
                elif card_ranks[hand1[2]] == card_ranks[hand2[2]]:
                    if card_ranks[hand1[3]] > card_ranks[hand2[3]]:
                        return True
                    elif card_ranks[hand1[3]] == card_ranks[hand2[3]]:
                        if card_ranks[hand1[4]] > card_ranks[hand2[4]]:
                            return True
                        elif card_ranks[hand1[4]] == card_ranks[hand2[4]]:
                            print("fuck - should not happen - trink ein Klosterbräu")
    return False        


deck_sorted = [deck[0]]

for draw in deck[1:]:
    inserted = False
    i = 0
    while not inserted:
        if i == len(deck_sorted):
            deck_sorted.append(draw)
            inserted = True
        elif is_first_hand_higher_than_second_hand(draw['hand'], deck_sorted[i]['hand']):
            deck_sorted.insert(i, draw)
            inserted = True
        i += 1
            
result = 0
rank = len(deck_sorted)
for draw in deck_sorted:
    result += rank * draw['bid']
    rank -= 1
    
print(f'{result=}')
# get max value
# max(freq.values())
# get key where value is max
# max(freq, key=freq.get)
