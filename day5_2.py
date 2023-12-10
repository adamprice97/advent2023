from util import read_txt

strs = ['seed-to-soil', 'soil-to-fertilizer',
         'fertilizer-to-water', 'water-to-light',
         'light-to-temperature','temperature-to-humidity',
         'humidity-to-location']

class converter():
    def __init__(self, in_, out_, range):
        self.in_ = int(in_)
        self.delta = int(out_) - self.in_
        self.max = (self.in_ + int(range)) - 1

    def convert(self, lower, upper):
        return int(lower) + self.delta, int(upper) + self.delta
   
maps_ = {s: [] for s in strs}

for line in read_txt('inputs/input5.txt'):
    if line == []: continue
    if 'seeds' in line[0]:
        seeds = line[1:]
    elif 'to' in line[0]:
        map_str = line[0]
    else:
        maps_[map_str].append(converter(line[1], line[0], line[2]))

#sort maps by input number for easier logic later
for str in strs:
    maps_[str].sort(key=lambda x: x.in_, reverse=False)

#convert seed list
uppers = []
lowers = []
for i in range(len(seeds)):
    if i % 2 == 1:
        lowers.append(int(seeds[i-1]))
        uppers.append(int(seeds[i-1])+int(seeds[i]))

#pass through maps
locations = []
for s in strs:
    l_tmp = []
    u_tmp = []
    for i in range(len(uppers)):
        lower = lowers[i]
        upper = uppers[i]
        for m in range(len(maps_[s])):
            if lower < maps_[s][m].in_:
                l_tmp.append(lower)
                if upper < maps_[s][m].in_:
                    u_tmp.append(upper)
                    break
                else:
                    u_tmp.append(maps_[s][m].in_)
                    lower = maps_[s][m].in_
            if lower >= maps_[s][m].in_ and lower <= maps_[s][m].max: 
                if upper > maps_[s][m].max:
                    l, u = maps_[s][m].convert(lower, maps_[s][m].max)
                    lower = maps_[s][m].max
                    l_tmp.append(l)
                    u_tmp.append(u)
                else:
                    l, u = maps_[s][m].convert(lower, upper)
                    l_tmp.append(l)
                    u_tmp.append(u)
                    break
        else: #upper goes over convertable inputs
            l_tmp.append(lower)
            u_tmp.append(upper)
    lowers = l_tmp
    uppers = u_tmp
print(min(lowers))