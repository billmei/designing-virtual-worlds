import cellular
import random

# Rule entries are of the form:
#     current, neighbor1, neighbor2, neighbor3, neighbor4, new
rules = [ [ 0, 0, 0, 0, 1, 2 ],
          [ 0, 0, 0, 0, 6, 3 ],
          [ 0, 0, 0, 0, 7, 1 ],
          [ 0, 0, 0, 1, 1, 2 ],
          [ 0, 0, 0, 1, 2, 2 ],
          [ 0, 0, 0, 1, 3, 2 ],
          [ 0, 0, 0, 2, 1, 2 ],
          [ 0, 0, 0, 2, 6, 2 ],
          [ 0, 0, 0, 2, 7, 2 ],
          [ 0, 0, 0, 5, 2, 5 ],
          [ 0, 0, 0, 6, 2, 2 ],
          [ 0, 0, 0, 7, 2, 2 ],
          [ 0, 0, 1, 0, 2, 2 ],
          [ 0, 0, 2, 1, 2, 5 ],
          [ 0, 0, 2, 3, 2, 2 ],
          [ 0, 0, 5, 2, 2, 2 ],
          [ 0, 1, 2, 3, 2, 1 ],
          [ 0, 1, 2, 4, 2, 1 ],
          [ 0, 1, 2, 5, 2, 5 ],
          [ 0, 1, 2, 6, 2, 1 ],
          [ 0, 1, 2, 7, 2, 1 ],
          [ 0, 1, 2, 7, 5, 1 ],
          [ 0, 1, 4, 2, 2, 1 ],
          [ 0, 1, 4, 3, 2, 1 ],
          [ 0, 1, 4, 4, 2, 1 ],
          [ 0, 1, 4, 7, 2, 1 ],
          [ 0, 1, 6, 2, 5, 1 ],
          [ 0, 1, 7, 2, 2, 1 ],
          [ 0, 1, 7, 2, 5, 5 ],
          [ 0, 1, 7, 5, 2, 1 ],
          [ 0, 1, 7, 6, 2, 1 ],
          [ 0, 1, 7, 7, 2, 1 ],
          [ 0, 2, 5, 2, 7, 1 ],
          [ 1, 0, 0, 0, 1, 1 ],
          [ 1, 0, 0, 0, 6, 1 ],
          [ 1, 0, 0, 0, 7, 7 ],
          [ 1, 0, 0, 1, 1, 1 ],
          [ 1, 0, 0, 1, 2, 1 ],
          [ 1, 0, 0, 2, 1, 1 ],
          [ 1, 0, 0, 2, 4, 4 ],
          [ 1, 0, 0, 2, 7, 7 ],
          [ 1, 0, 0, 5, 1, 1 ],
          [ 1, 0, 1, 0, 1, 1 ],
          [ 1, 0, 1, 1, 1, 1 ],
          [ 1, 0, 1, 2, 4, 4 ],
          [ 1, 0, 1, 2, 7, 7 ],
          [ 1, 0, 2, 0, 2, 6 ],
          [ 1, 0, 2, 1, 2, 1 ],
          [ 1, 0, 2, 2, 1, 1 ],
          [ 1, 0, 2, 2, 4, 4 ],
          [ 1, 0, 2, 2, 6, 3 ],
          [ 1, 0, 2, 2, 7, 7 ],
          [ 1, 0, 2, 3, 2, 7 ],
          [ 1, 0, 2, 4, 2, 4 ],
          [ 1, 0, 2, 6, 2, 6 ],
          [ 1, 0, 2, 6, 4, 4 ],
          [ 1, 0, 2, 6, 7, 7 ],
          [ 1, 0, 2, 7, 2, 7 ],
          [ 1, 0, 5, 4, 2, 7 ],
          [ 1, 1, 1, 1, 2, 1 ],
          [ 1, 1, 1, 2, 2, 1 ],
          [ 1, 1, 1, 2, 4, 4 ],
          [ 1, 1, 1, 2, 5, 1 ],
          [ 1, 1, 1, 2, 6, 1 ],
          [ 1, 1, 1, 2, 7, 7 ],
          [ 1, 1, 1, 5, 2, 2 ],
          [ 1, 1, 2, 1, 2, 1 ],
          [ 1, 1, 2, 2, 2, 1 ],
          [ 1, 1, 2, 2, 4, 4 ],
          [ 1, 1, 2, 2, 5, 1 ],
          [ 1, 1, 2, 2, 7, 7 ],
          [ 1, 1, 2, 3, 2, 1 ],
          [ 1, 1, 2, 4, 2, 4 ],
          [ 1, 1, 2, 6, 2, 1 ],
          [ 1, 1, 2, 7, 2, 7 ],
          [ 1, 1, 3, 2, 2, 1 ],
          [ 1, 2, 2, 2, 4, 4 ],
          [ 1, 2, 2, 2, 7, 7 ],
          [ 1, 2, 2, 4, 3, 4 ],
          [ 1, 2, 2, 5, 4, 7 ],
          [ 1, 2, 3, 2, 4, 4 ],
          [ 1, 2, 3, 2, 7, 7 ],
          [ 1, 2, 4, 2, 5, 5 ],
          [ 1, 2, 4, 2, 6, 7 ],
          [ 1, 2, 5, 2, 7, 5 ],
          [ 2, 0, 0, 0, 1, 2 ],
          [ 2, 0, 0, 0, 2, 2 ],
          [ 2, 0, 0, 0, 4, 2 ],
          [ 2, 0, 0, 0, 7, 1 ],
          [ 2, 0, 0, 1, 2, 2 ],
          [ 2, 0, 0, 1, 5, 2 ],
          [ 2, 0, 0, 2, 1, 2 ],
          [ 2, 0, 0, 2, 2, 2 ],
          [ 2, 0, 0, 2, 3, 2 ],
          [ 2, 0, 0, 2, 4, 2 ],
          [ 2, 0, 0, 2, 6, 2 ],
          [ 2, 0, 0, 2, 7, 2 ],
          [ 2, 0, 0, 3, 2, 6 ],
          [ 2, 0, 0, 4, 2, 3 ],
          [ 2, 0, 0, 5, 1, 7 ],
          [ 2, 0, 0, 5, 2, 2 ],
          [ 2, 0, 0, 5, 7, 5 ],
          [ 2, 0, 0, 7, 2, 2 ],
          [ 2, 0, 1, 0, 2, 2 ],
          [ 2, 0, 1, 1, 2, 2 ],
          [ 2, 0, 1, 2, 2, 2 ],
          [ 2, 0, 1, 4, 2, 2 ],
          [ 2, 0, 1, 7, 2, 2 ],
          [ 2, 0, 2, 0, 2, 2 ],
          [ 2, 0, 2, 0, 3, 2 ],
          [ 2, 0, 2, 0, 5, 2 ],
          [ 2, 0, 2, 0, 7, 3 ],
          [ 2, 0, 2, 1, 2, 2 ],
          [ 2, 0, 2, 1, 5, 2 ],
          [ 2, 0, 2, 2, 1, 2 ],
          [ 2, 0, 2, 2, 2, 2 ],
          [ 2, 0, 2, 2, 7, 2 ],
          [ 2, 0, 2, 3, 2, 1 ],
          [ 2, 0, 2, 4, 2, 2 ],
          [ 2, 0, 2, 4, 5, 2 ],
          [ 2, 0, 2, 5, 5, 2 ],
          [ 2, 0, 2, 6, 2, 2 ],
          [ 2, 0, 2, 7, 2, 2 ],
          [ 2, 0, 3, 1, 2, 2 ],
          [ 2, 0, 3, 2, 1, 6 ],
          [ 2, 0, 3, 2, 2, 6 ],
          [ 2, 0, 3, 4, 2, 2 ],
          [ 2, 0, 4, 2, 2, 2 ],
          [ 2, 0, 5, 1, 2, 2 ],
          [ 2, 0, 5, 2, 1, 2 ],
          [ 2, 0, 5, 2, 2, 2 ],
          [ 2, 0, 5, 5, 2, 1 ],
          [ 2, 0, 5, 7, 2, 5 ],
          [ 2, 0, 6, 2, 2, 2 ],
          [ 2, 0, 6, 7, 2, 2 ],
          [ 2, 0, 7, 1, 2, 2 ],
          [ 2, 0, 7, 2, 2, 2 ],
          [ 2, 0, 7, 4, 2, 2 ],
          [ 2, 0, 7, 7, 2, 2 ],
          [ 2, 1, 1, 2, 2, 2 ],
          [ 2, 1, 1, 2, 6, 1 ],
          [ 2, 1, 2, 2, 2, 2 ],
          [ 2, 1, 2, 2, 4, 2 ],
          [ 2, 1, 2, 2, 6, 2 ],
          [ 2, 1, 2, 2, 7, 2 ],
          [ 2, 1, 4, 2, 2, 2 ],
          [ 2, 1, 5, 2, 2, 2 ],
          [ 2, 1, 6, 2, 2, 2 ],
          [ 2, 1, 7, 2, 2, 2 ],
          [ 2, 2, 2, 2, 7, 2 ],
          [ 2, 2, 2, 4, 4, 2 ],
          [ 2, 2, 2, 4, 6, 2 ],
          [ 2, 2, 2, 7, 6, 2 ],
          [ 2, 2, 2, 7, 7, 2 ],
          [ 3, 0, 0, 0, 1, 3 ],
          [ 3, 0, 0, 0, 2, 2 ],
          [ 3, 0, 0, 0, 4, 1 ],
          [ 3, 0, 0, 0, 7, 6 ],
          [ 3, 0, 0, 1, 2, 3 ],
          [ 3, 0, 0, 4, 2, 1 ],
          [ 3, 0, 0, 6, 2, 2 ],
          [ 3, 0, 1, 0, 2, 1 ],
          [ 3, 0, 2, 5, 1, 1 ],
          [ 4, 0, 2, 2, 2, 1 ],
          [ 4, 0, 2, 3, 2, 6 ],
          [ 4, 0, 3, 2, 2, 1 ],
          [ 5, 0, 0, 0, 2, 2 ],
          [ 5, 0, 0, 2, 1, 5 ],
          [ 5, 0, 0, 2, 2, 5 ],
          [ 5, 0, 0, 2, 3, 2 ],
          [ 5, 0, 0, 2, 7, 2 ],
          [ 5, 0, 2, 0, 2, 2 ],
          [ 5, 0, 2, 1, 2, 2 ],
          [ 5, 0, 2, 1, 5, 2 ],
          [ 5, 0, 2, 2, 4, 4 ],
          [ 5, 0, 2, 7, 2, 2 ],
          [ 5, 1, 2, 1, 2, 2 ],
          [ 5, 1, 2, 4, 2, 2 ],
          [ 5, 1, 2, 7, 2, 2 ],
          [ 6, 0, 0, 0, 1, 1 ],
          [ 6, 0, 0, 0, 2, 1 ],
          [ 6, 1, 2, 1, 2, 5 ],
          [ 6, 1, 2, 1, 3, 1 ],
          [ 6, 1, 2, 2, 2, 5 ],
          [ 7, 0, 0, 0, 7, 7 ],
          [ 7, 0, 2, 2, 2, 1 ],
          [ 7, 0, 2, 2, 5, 1 ],
          [ 7, 0, 2, 3, 2, 1 ],
          [ 7, 0, 2, 5, 2, 5 ] ]

# Create a blank table.
states=8
table = [None] * states
for a in range(states):
    table[a] = [None] * states
    for b in range(states):
        table[a][b] = [None] * states
        for c in range(states):
            table[a][b][c] = [None] * states
            for d in range(states):
                table[a][b][c][d] = [0] * states

# Now fill the table
for rule in rules:
    current, n1, n2, n3, n4, new = rule
    # The rules are independent of orientation.
    table[current][n1][n2][n3][n4] = new
    table[current][n2][n3][n4][n1] = new
    table[current][n3][n4][n1][n2] = new
    table[current][n4][n1][n2][n3] = new
# the above code was taken from http://www.alcyone.com/software/cage/

class Cell(cellular.Cell):
  value=0
  def update(self):
    count=0
    curr=self.value
    n,e,s,w=self.neighbours
    self.value=table[curr][n.value][e.value][s.value][w.value]

  def load(cell,text):
    if text==' ': cell.value=0
    else: cell.value=int(text)
  def save(cell):
    return '%d'%cell.value
  def colour(cell):
    return ['white',
            'blue',
            'red',
            'yellow',
            'green',
            'cyan',
            'magenta',
            'black'
            ][cell.value]
  def randomize(cell):
    cell.value=random.randrange(8)
  def copy(cell,other):
    cell.value=other.value

world=cellular.World(Cell,80,80,directions=4)
world.load('langton.txt')
world.display.activate(size=5)
while 1:
  world.update()






