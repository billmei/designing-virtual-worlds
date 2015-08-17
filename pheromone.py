import phAnts

# The following parameters can be set (and are shown with their default values)
#        map='phAnts.txt',
#        dispersionRate=0.04,
#        evaporationRate=0.99,
#        basePherAmount=0.2,
#        pherDecay=0.8,
#        turnCertainty=10,
#        antCount=10,
#        time=1000,
#        height=30,
#        width=30,
#        displaySize=10            (set this to 0 for no display)
#
#
# For example, if you want to run it with 20 ants and no display, you could say:
#   phAnts.run(antCount=20, displaySize=0)
#
# For a 50x50 world where the ants drop lots more pheromone, and using a
#  different map:
#   phAnts.run(width=50, height=50, basePherAmount=1.0, map='lotsOfFood.txt')

foodCount=phAnts.run()
print foodCount
