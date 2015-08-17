import cellular
import random

class Cell(cellular.Cell):
    value=0

    def update(self):
        count=0
        for n in self.neighbours:
            if n.value!=0: count+=1
        if self.value==0:
            if count==3:
                self.value=1
        else:
            if count<2 or count>3:
                self.value=0

    def colour(self):
        if self.value==0: return 'white'
        else: return 'black'

    def load(self,text):
        if text=='X': self.value=1
        else: self.value=0
    def save(self):
        if self.value==0: return ' '
        else: return 'X'

    def randomize(self):
        self.value=random.choice([0,1])


world=cellular.World(Cell,width=50,height=50)
world.randomize()
world.display.activate(size=5)
while 1:
    world.update()




