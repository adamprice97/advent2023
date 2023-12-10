from util import read_txt
import numpy as np

hands_strs = []
bets = []
for line in read_txt('inputs/input7.txt'):
    hands_strs.append(line[0])
    bets.append(int(line[1]))

#Value the hands by giving their value in base five
def card_value(hand):
    product =  np.zeros(1, dtype=np.float64) # overflow error on normal var
    hand = np.flip(hand)
    for i in range(5):
        product[0] += (i+1)**13 * hand[i]
    return product

histo_hands = []
int_hands = []
for hand in hands_strs:
    histo_hand = np.zeros(13) #Turn hands into histograms
    int_hand = []
    for c in hand:
        if c == 'A':
            histo_hand[12] += 1
            int_hand.append(12)
        elif c =='K':
            histo_hand[11] += 1
            int_hand.append(11)
        elif c =='Q':
            histo_hand[10] += 1
            int_hand.append(10)
        elif c =='J':
            histo_hand[9] += 1
            int_hand.append(9)
        elif c =='T':
            histo_hand[8] += 1
            int_hand.append(8)
        else:
            histo_hand[int(c)-2] += 1
            int_hand.append(int(c)-2)
    histo_hands.append(histo_hand)
    int_hands.append(int_hand)

def score_hand(hand):
    if np.sum(np.isin(hand, 5)):
        return 6
    if np.sum(np.isin(hand, 4)):
        return 5
    three_of_a_kind = np.isin(hand, 3)
    pair = np.isin(hand, 2)
    if np.sum(pair) and np.sum(three_of_a_kind):
        return 4
    if np.sum(three_of_a_kind):
        return 3
    if np.sum(pair) >= 2:
        return 2
    if np.sum(pair):
        return 1
    return 0

scores = np.zeros(len(histo_hands))
card_vals = np.zeros(len(histo_hands))
for i in range(len(histo_hands)):
    scores[i] = score_hand(np.array(histo_hands[i]))
    card_vals[i] = card_value(np.array(int_hands[i], dtype=np.float64))

ranks = np.zeros(scores.shape[0])
rank = scores.shape[0]
for i in range(int(scores.max()),-1,-1):
    draws = np.where(scores==i)[0]
    for h in np.flip(np.sort(card_vals[draws])):
        #assume every hand is unique
        #print(np.where(card_vals==h))
        ranks[np.where(card_vals==h)[0]] = rank
        rank -= 1

result = 0
for i in range(ranks.shape[0]):
    result += ranks[i] * bets[i]

print(result)