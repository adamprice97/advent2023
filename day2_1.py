from util import read_txt2
import re

class round():
    def __init__(self, round_string):
        self.blue = 0
        self.red = 0 
        self.green = 0
        for boxes in round_string.split(','):
            if 'blue' in boxes:
                self.blue = int(re.sub('\D', '', boxes))
            elif 'red' in boxes:
                self.red = int(re.sub('\D', '', boxes))
            elif 'green' in boxes:
                self.green = int(re.sub('\D', '', boxes))

class game():
    def __init__(self, line, ID):
        split = line.split(':')
        self.ID = ID
        self.rounds = [round(s) for s in split[1].split(';')]
    
    def maxes(self):
        self.blue = 0
        self.red = 0 
        self.green = 0
        for r in self.rounds:
            if r.blue > self.blue:
                self.blue = r.blue
            if r.red > self.red:
                self.red = r.red
            if r.green > self.green:
                self.green = r.green
        return self.blue, self.red, self.green

input_ = read_txt2('inputs/input2.txt')
blues = 14
reds = 12
greens = 13

games = []
for i, l in enumerate(input_):
    games.append(game(l, i+1))

game_sum = 0
for g_ in games:
    b, r, g = g_.maxes()
    #print(b, r, g)
    if b <= blues and r <= reds and g <= greens:
        game_sum += g_.ID
        print(g_.ID)
print(game_sum)