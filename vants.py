import cellular

class Cell(cellular.Cell):
  state=0
  def colour(self):
    if self.state==0: return 'black'
    else: return 'green'

class Vant(cellular.Agent):
  colour='blue'
  def update(self):
    if self.cell.state==0:
      self.cell.state=1
      self.turnRight()
      self.goForward()
    else:
      self.cell.state=0
      self.turnLeft()
      self.goForward()


world=cellular.World(Cell,width=200,height=200,directions=4)
world.addAgent(Vant(),x=50,y=50,dir=0)

world.display.activate(size=3)
while 1:
    world.update()



