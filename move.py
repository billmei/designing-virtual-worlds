import cellular
import random

class Cell(cellular.Cell):
  def __init__(self):
    self.value=0
  def update(self):
    count=0
    for c in self.neighbours:
      if c.value==1: count+=1
    if self.value==1:
      if count!=2 and count!=4 and count!=5:
        self.value=0
    else:
      if count==3 or count==6 or count==8:
        self.value=1

  def load(self,text):
    if text==' ': self.value=0
    else: self.value=1
  def colour(self):
    if self.value==0: return 'white'
    else: return 'black'
  def randomize(self):
    self.value=random.choice([0,1])

world=cellular.World(Cell,40,30)
world.randomize()
world.display.activate(size=10)
world.display.delay=1
while 1:
  world.update()




