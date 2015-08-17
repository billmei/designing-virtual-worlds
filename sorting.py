import cellular
import random
import math

numAgents=20

memoryLength=15
k_pickup=0.1
k_drop=0.3

empty='white'
types=[('green',200),('blue',200)]

class Cell(cellular.Cell):
  contents=empty
  def colour(self):
    return self.contents

class Agent(cellular.Agent):
  def __init__(self):  # this is automatically run when the Agent is created
    self.memory=[empty]*memoryLength
    self.carrying=empty
  def update(self):
    # update our memory
    self.memory.append(self.cell.contents)
    del self.memory[0]


    # check if we can drop something
    if self.cell.contents==empty and self.carrying!=empty:
      # calculate the probability for dropping
      f=float(self.memory.count(self.carrying))/memoryLength
      p=math.pow(f/(k_drop+f),2)
      if random.random()<p:
        # drop it
        self.cell.contents=self.carrying
        self.carrying=empty
    # check if we can pick something up
    elif self.cell.contents!=empty and self.carrying==empty:
      # calculate the probability for picking it up
      f=float(self.memory.count(self.cell.contents))/memoryLength
      p=math.pow(k_pickup/(k_pickup+f),2)
      if random.random()<p:
        # pick it up
        self.carrying=self.cell.contents
        self.cell.contents=empty

    # move randomly
    self.goInDirection(random.randrange(4))
  def colour(self):
    return self.carrying


world=cellular.World(Cell,width=80,height=50,directions=4)
for type,count in types:
  for i in range(count):
    x=random.randrange(world.width)
    y=random.randrange(world.height)
    world.getCell(x,y).contents=type

for i in range(numAgents):
  world.addAgent(Agent())

world.display.activate(size=5)
while 1:
    world.update()



