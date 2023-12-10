from util import read_txt
import numpy as np

def solve(lines):
    nums = []
    row_max = lines.shape[0] - 1
    column_max = len(lines[0][0]) - 1
    print(row_max, column_max)
    for r in range(row_max+1):
        num = ''
        valid = False
        for c in range(column_max+1):
            if lines[r][0][c].isdigit():
                num += lines[r][0][c]
                if valid == False: #is there a symbol near 
                    for r_ in range(r-1, r+2):
                        r__ = np.max([0, np.min([r_, row_max])])
                        for c_ in range(c-1, c+2):
                            c__ = np.max([0, np.min([c_, column_max])])
                            if not lines[r__][0][c__].isdigit() and lines[r__][0][c__] != '.':
                                valid = True
                                break
                        else:
                            continue
                        break
            else:
                if num != '' and valid:
                    print(num)
                    nums.append(int(num))
                num = ''
                valid = False
        if num != '' and valid:
            print(num)
            nums.append(int(num))
        num = ''
        valid = False
    return sum(nums)

input_ = read_txt('inputs/input3.txt')
print(solve(np.array(input_)))