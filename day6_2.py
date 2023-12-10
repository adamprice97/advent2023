from util import read_txt

for line in read_txt('inputs/input6.txt'):
    if line[0] == 'Time:':
        times = line[1:]
    else:
        distances = line[1:]

time = int("".join(times))
distance = int("".join(distances))

valids = []
for ms in range(time):
    if ms * (time-ms) > distance:
        valids.append(ms)

print(len(valids))
