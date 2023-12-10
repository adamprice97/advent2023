from util import read_txt
import numpy as np

input_ = read_txt('inputs/input4.txt')

winning_nums = [line[2:12] for line in input_]
player_nums = [line[13:] for line in input_]

total = 0
for card in range(len(winning_nums)):
    count = 0
    for pn in player_nums[card]:
        if pn in winning_nums[card]:
            count += 1
    total += np.floor(2**(count-1))

print(total)