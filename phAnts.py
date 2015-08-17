import cellular
import random
import math

class Cell(cellular.Cell):
  dispersionRate=0.04
  evaporationRate=0.99

  def __init__(self):
    self.isHome=0
    self.isFood=0
    self.homePher=0.0
    self.foodPher=0.0
  def update(self):
    htotal=0
    ftotal=0
    for c in self.neighbours:
      htotal+=c.homePher
      ftotal+=c.foodPher
    havg=htotal/len(self.neighbours)
    favg=ftotal/len(self.neighbours)
    self.homePher+=(havg-self.homePher)*Cell.dispersionRate
    self.foodPher+=(favg-self.foodPher)*Cell.dispersionRate
    self.homePher*=Cell.evaporationRate
    self.foodPher*=Cell.evaporationRate
    if self.homePher>1: self.homePher=1.0
    if self.foodPher>1: self.foodPher=1.0
    if self.homePher<0.001: self.homePher=0.0
    if self.foodPher<0.001: self.foodPher=0.0

  def colour(self):
    if self.isHome: return 'red'
    if self.isFood: return 'blue'
    # if it isn't one of these two cases, we need to make a colour that's
    # a combination of red and blue
    return (self.homePher,0,self.foodPher)

  def load(self,text):
    self.isHome=0
    self.isFood=0
    if text=='H': self.isHome=1
    if text=='F': self.isFood=1

class Agent(cellular.Agent):
  basePherStrength=0.4
  pherDecay=0.8
  turnCertainty=10
  
  colour='green'

  def __init__(self):
    self.hasFood=0
    self.pherStrength=self.basePherStrength
    self.foodCount=0
  def update(self):
    # change state if we've reached what we are looking for
    if self.hasFood:
      self.cell.foodPher+=self.pherStrength
      if self.cell.foodPher>1.0: self.cell.foodPher=1.0
      self.pherStrength*=self.pherDecay
      if self.cell.isHome:
        self.hasFood=0
        self.pherStrength=self.basePherStrength
        self.turnAround()
        self.foodCount+=1
    else:
      self.cell.homePher+=self.pherStrength
      if self.cell.homePher>1.0: self.cell.homePher=1.0
      self.pherStrength*=self.pherDecay
      if self.cell.isFood:
        self.hasFood=1
        self.pherStrength=self.basePherStrength
        self.turnAround()

    # figure out if we should turn
    around=[self.aheadCell,self.rightCell,self.leftCell]
    sense=[0,0,0]
    for i in [-1,0,1]:  # left, ahead, right
      if not self.hasFood:
        if around[i].isFood: sense[i]=1
        else: sense[i]=min(around[i].foodPher,1)
      else:
        if around[i].isHome: sense[i]=1
        else: sense[i]=min(around[i].homePher,1)

    # adjust the values based on the turning certainty
    sense=[math.pow(x,self.turnCertainty) for x in sense]

    #make a decision to turn
    total=sense[0]+sense[1]+sense[-1]
    if total==0:  # if I can't sense anything, turn randomly
      pLeft=1.0/3
      pRight=1.0/3
    else:
      pLeft=sense[-1]/total
      pRight=sense[1]/total
    r=random.random()
    if r<pLeft:
      self.turnLeft()
    elif r<pLeft+pRight:
      self.turnRight()

    self.goForward()





def run(map='phAnts.txt',
        dispersionRate=0.04,
        evaporationRate=0.99,
        basePherAmount=0.2,
        pherDecay=0.8,
        turnCertainty=10,
        antCount=10,
        time=1000,
        height=30,
        width=30,
        displaySize=10):
  Cell.dispersionRate=dispersionRate
  Cell.evaporationRate=evaporationRate
  Agent.basePherStrength=basePherAmount
  Agent.pherDecay=pherDecay
  Agent.turnCertainty=turnCertainty

  world=cellular.World(Cell,width,height)
  world.load(map)

  # figure out where to put the ants (they should start at home)
  homes=[]
  for i in range(width):
    for j in range(height):
      if world.grid[i][j].isHome: homes.append((i,j))
  for i in range(antCount):
    ant=Agent()
    i,j=random.choice(homes)
    world.addAgent(ant,x=i,y=j)

  if displaySize:
    world.display.activate(size=displaySize)

  # run the simulation
  for i in range(time):
    world.update()

  # figure out how much food was gathered per ant
  totalFood=0.0
  for a in world.agents:
    totalFood+=a.foodCount
  return totalFood/antCount

