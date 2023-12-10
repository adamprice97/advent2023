from util import read_txt

for line in read_txt('inputs/input6.txt'):
    if line[0] == 'Time:':
        times = line[1:]
    else:
        distances = line[1:]

valids = [[] for _ in range(len(times))]
for race in range(len(times)):
    for ms in range(int(times[race])):
        if ms * (int(times[race])-ms) > int(distances[race]):
            valids[race].append(ms)

product = 1
for l in valids:
    product *= len(l)
print(product)