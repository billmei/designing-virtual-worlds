import cellular
import random

class Cell(cellular.Cell):
    def __init__(self):
        self.value=0
    def update(self):
        if self.value==1:
            self.value=0
        else:
            count=0
            for n in self.neighbours:
                if n.value==1:
                    count+=1
            if count==2:
                self.value=1

    def load(self,data):
        if data==' ': self.value=0
        else: self.value=1

    def colour(self):
        if self.value==0: return 'white'
        else: return 'black'

    def randomize(self):
        if random.random()<0.5:
            self.value=0
        else:
            self.value=1


world=cellular.World(Cell,width=20,height=40)
world.load('seeds.txt')
world.display.activate(size=10)
world.display.delay=8
while 1:
    world.update()



