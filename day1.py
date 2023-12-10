from util import read_txt


number_strs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_nums_sum(line):
    l = 0
    l_num = -1
    while l_num == -1:
        if line[l].isdigit():
            l_num = int(line[l])*10
            break
        for i, n in enumerate(number_strs):
            if n == line[l:l+len(n)]:
                l_num = (i+1)*10
        l += 1

    r = len(line) - 1
    r_num = -1
    while r_num == -1:
        if line[r].isdigit():
            r_num = int(line[r])
            break
        for i, n in enumerate(number_strs):
            if n in line[r-(len(n)-1):r+1]:
                r_num = i+1
        r -= 1
    return l_num + r_num

input_ = read_txt('inputs/input1.txt')
sum_ = 0
for l in input_:
    sum_ += get_nums_sum(l[0])
print(sum_)