from util import read_txt

strs = ['seed-to-soil', 'soil-to-fertilizer',
         'fertilizer-to-water', 'water-to-light',
         'light-to-temperature','temperature-to-humidity',
         'humidity-to-location']

class converter():
    def __init__(self, in_, out_, range):
        self.in_ = int(in_)
        self.out_ = int(out_)
        self.range = int(range)

    def is_in(self, val):
        return int(val) >= self.in_ and (int(val)-self.in_) < self.range
    
    def convert(self, val):
        return int(val) + (self.out_ - self.in_)

maps_ = {s: [] for s in strs}

for line in read_txt('inputs/input5.txt'):
    if line == []: continue
    if 'seeds' in line[0]:
        seeds = line[1:]
    elif 'to' in line[0]:
        map_str = line[0]
    else:
        maps_[map_str].append(converter(line[1], line[0], line[2]))

print('solve')

#pass through maps
locations = []
for s in seeds:
    l = s 
    for m in strs:
        for r in maps_[m]:
            if r.is_in(l):
                l = r.convert(l)
                print('mapped', l)
                break
    locations.append(l)
    #exit()
print(min(locations))