#Austin Peterson
#Python3
#CSE355

import numpy
#dep
import matplotlib.pyplot as pyplot
from matplotlib import animation

#constant for cell grid size
N = 0#16std. wolf size
M = 0#31

#more running
print("Welcome to The Cellular Automata\n")
ruleset = input("Please enter ruleset(#): ")
N  = int(input("Please enter a depth: "))
M = int(input("Please enter a width: "))

#glbl start grid
#beginning wolfram matrix
grid = numpy.zeros((N, M), numpy.int8)#int8 and using -1s so overflow
grid[0,int((M-1)/2)] = -1

#parse rules into binary
wolframRule = "{0:08b}".format(int(ruleset))

wolframRule = list(wolframRule)
#print(wolframRule)

contFlag = False






#func to lookup user rule
def ruleLook(i):
    #print(i)ß
    if wolframRule[i] == '1':
        return -1
    else:
        return 0


#passable func
#passed to animation (matplotlib)
def update(data):
    global grid#copy grid for safekeeping:)
    newGrid = grid.copy()
    
    #skip first row
    for i in range(1, N):
        for j in range(M):
            #harvest neighbors (&self)
            #
            c = grid[(i-1)%N, j]#swapped M and N
            r = grid[(i-1)%N, (j+1)%M]
            l = grid[(i-1)%N, (j-1)%M]
            
            if l == -1 and c == -1 and l == -1:     #111
                newGrid[i, j] = ruleLook(0)
                #newGrid[i,j] = -1
            
            if l == -1 and c == -1 and r == 0:   #110
                newGrid[i, j] = ruleLook(1)
            
            if l == -1 and c == 0 and r == -1:   #101
                newGrid[i, j] = ruleLook(2)
            
            if l == -1 and c == 0 and r == 0:  #100
                newGrid[i, j] = ruleLook(3)
            
            if l == 0 and c == -1 and r == -1:   #011
                newGrid[i, j] = ruleLook(4)
            
            if l == 0 and c == -1 and r == 0:   #010
                newGrid[i, j] = ruleLook(5)
            
            if l == 0 and c == 0 and r == -1:   #001
                newGrid[i, j] = ruleLook(6)
            
            if l == 0 and c == 0 and r == 0:  #000
                newGrid[i, j] = ruleLook(7)

    #check grid vs newGrid here to finish animation
    for i in range(1, N):
        for j in range(M):
            if grid[i, j] != newGrid[i, j]:
                contFlag = True
            else:
                contFlag = False


    if contFlag == True:
        print("finshed.")
        #inp = input("Done looking? ")

    mat.set_data(newGrid)
    grid = newGrid#update
    return mat






fig, axes = pyplot.subplots()

mat = axes.matshow(grid)#builds grid on subplot
ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)#animation
#the money
pyplot.show()



