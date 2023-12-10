from util import read_txt
import numpy as np
import string

def num_mask(lines):
    row_max = lines.shape[0] 
    column_max = len(lines[0][0]) 
    id = 1
    mask = np.zeros((row_max, column_max))
    nums = {}
    for r in range(row_max):
        num = ''
        for c in range(column_max):
            if lines[r][0][c].isdigit():
                mask[r,c] = id
                num+=lines[r][0][c]
            else:
                if num != '':
                    nums[id] = int(num)
                    num = ''
                    id += 1
        if num != '':
            nums[id] = int(num)
            num = ''
            id += 1
    return mask, nums

def solve(lines):
    sum_ = 0
    row_max = lines.shape[0] - 1
    column_max = len(lines[0][0]) - 1
    mask, nums = num_mask(lines)
    for r in range(row_max+1):
        for c in range(column_max+1):
            if lines[r][0][c] == '*':
                gears = []
                for r_ in range(r-1, r+2):
                    r__ = np.max([0, np.min([r_, row_max])])
                    for c_ in range(c-1, c+2):
                        c__ = np.max([0, np.min([c_, column_max])])
                        if mask[r__,c__] > 0:
                            if mask[r__,c__] not in gears:
                                gears.append(mask[r__,c__])  
                if len(gears) == 2:
                    sum_ += nums[gears[0]] * nums[gears[1]]
 
    return sum_

input_ = read_txt('inputs/input3.txt')
print(solve(np.array(input_)))