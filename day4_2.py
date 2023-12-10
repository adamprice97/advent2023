from util import read_txt
import numpy as np

input_ = read_txt('inputs/input4.txt')

track_cards = np.ones(len(input_))
winning_nums = [line[2:12] for line in input_]
player_nums = [line[13:] for line in input_]

total = 0
for i, card in enumerate(range(len(winning_nums))):
    matches = 0
    for pn in player_nums[card]:
        if pn in winning_nums[card]:
            matches += 1
    for k in range(0, matches):
        track_cards[i+k+1] += (1 * track_cards[i])

print(track_cards)
print(track_cards.sum())