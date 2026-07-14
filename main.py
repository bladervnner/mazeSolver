from collections import deque
import heapq
from dataclasses import dataclass
import time
import os
import math

ANIMATE = True # set to False to turn off animation in the function visitPoint

class Point:
    '''Creating a point class in coordinate format using x and y'''
    '''This works well with our maze since it is a 2D array and we can use the x and y coordinates to find the point in the maze'''
    # 
    def __init__(self, x: int, y: int):
        # define x and y vars
        self.X = x
        self.Y = y

    # Translate Point by adding x and y to the current point's x and y
    def translate(self, dx: int, dy: int):
        self.X += dx
        self.Y += dy
    
    # move Point by setting x and y to the current point's x and y
    def move(self, x: int, y: int):
        self.X = x
        self.Y = y

    # Print out the point in coordinate format
    def __str__(self):
        return f"({self.X}, {self.Y})"
    

    # TODO: Add functionality to Point Class like finding distance, etc in case we need help implementing A* or Dijkstra's algorithm for maze solving

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.X == other.X and self.Y == other.Y
        
    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt((dx * dx) + (dy * dy))


# Function param takes an int chosen by user and reads the maze and returnds a 2D array of file as maze
def readMaze (mazeNum: int):
    l=0
    # concatenate file name to read
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mazeNumString = os.path.join(script_dir, f"maze{mazeNum}.txt")
    # Reading file
    try:
        with open(mazeNumString, "r") as file:
            lines = file.readlines()
    except FileNotFoundError as e:
        print(f"Error caught: {e}")
        return None

    # Initialize 2D grid using num of lines in file and the length of the line
    cols, rows = len(lines[0]), len(lines)
    grid = [['*' for x in range(cols)] for y in range (rows)] # goes cols, then rows
    ## Changed the above 0 to an '*' to fill the grid with * instead of 0 as the last character in the maze was 0, need to find the bug and make it more elegant

    # Filling out 2D grid now with file contents
    for line in lines:
        c = 0 # char index
        for char in list(line):
            grid[l][c] = char
            c +=1
        l += 1

    return grid

# To Test readMaze
num = input("Pick a number between 1-3: ")
print(readMaze(num))


# Pass 2D array maze and display the current state
def displayMaze(maze: list[list[str]]):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], end="")


# To Test displayMaze
num = input("Pick a number between 1-3: ")
displayMaze(readMaze(num))

## This method passes our maze and finds the start point, returning them as a Point 
def findStart(maze: list[list[str]]):
    x = 0
    y = 0

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 's':
                x = i
                y = j
    
    startPoint = Point(x,y)
    return startPoint

#creating helper function to get the neighbors of a point in the maze to modularize the code

def getNeighbors(point: Point, maze: list[list[str]]):
            currPoint = point
            neighbors = []

            ''' This is not needed now
            # This checks if current point is a space
            if(maze[currPoint.X][currPoint.Y] == ' '):
                neighbors.append(Point(currPoint.X, currPoint.Y))
            '''

            # Checks the point above the current point
            if maze[currPoint.X - 1][currPoint.Y] == ' ' or maze[currPoint.X - 1][currPoint.Y] == 'f':
                neighbors.append(Point(currPoint.X - 1, currPoint.Y))            

            # Checks the point below the current point
            if maze[currPoint.X + 1][currPoint.Y] == ' ' or maze[currPoint.X + 1][currPoint.Y] == 'f':
                neighbors.append(Point(currPoint.X + 1, currPoint.Y))

            # Checks the point to the left of the current point
            if maze[currPoint.X][currPoint.Y - 1] == ' ' or maze[currPoint.X][currPoint.Y - 1] == 'f':
                neighbors.append(Point(currPoint.X, currPoint.Y - 1))
            
            # Checks the point to the right of the current point
            if maze[currPoint.X][currPoint.Y + 1] == ' ' or maze[currPoint.X][currPoint.Y + 1] == 'f':
                neighbors.append(Point(currPoint.X, currPoint.Y + 1))

            return neighbors

# Create helper functiont to mark if a point has been visited in the maze to modularize the code
def visitPoint(point: Point, maze: list[list[str]]):
    if maze[point.X][point.Y] == ' ':
        maze[point.X][point.Y] = '.'
    
    # will be benchmarking so may need to remove the displayMaze and time.sleep for performance testing
    if ANIMATE:
        os.system('cls')     
        displayMaze(maze)
        time.sleep(0.1) # 0.2 seconds delay to make it visual, but will slow down the algorithm significantly

# This method will be use dfs to solve the maze, with the paramater the maze
def dfs(maze: list[list[str]]):
    # creating Stack to hold Points visited
    pointsVisited = deque() # using deque as a stack to hold Points
    pointsVisited.append(findStart(maze)) # appending the start point to the stack
    iterations = 0

    while pointsVisited:
        iterations +=1
        currPoint = pointsVisited.pop() # pop the last point visited
        
        if maze[currPoint.X][currPoint.Y] == 'f':
            print("Maze solved!")
            print(f"Iterations: {iterations}")
            break
        
        visitPoint(currPoint, maze) # mark the current point as visited

        neighbors = getNeighbors(currPoint, maze) # get the neighbors of the current point

        for neighbor in neighbors:
            pointsVisited.append(neighbor) # add the neighbor to the stack


    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], end="")

    print(f"Iterations: {iterations}")


# This method will be use bfs to solve the maze, with the paramater the maze
def bfs(maze: list[list[str]]):
    # creating Queue to hold Points visited
    pointsVisited = deque() # using deque as a queue to hold Points
    pointsVisited.append(findStart(maze)) # appending the start point to the queue
    maze[pointsVisited[0].X][pointsVisited[0].Y] = '.' # changing our start point to a '.' to show we have visited it
    iterations = 0

    while pointsVisited:
        iterations +=1
        currPoint = pointsVisited.popleft() # pop the first point visited
        
        if maze[currPoint.X][currPoint.Y] == 'f':
            print("Maze solved!")
            print(f"Iterations: {iterations}")
            break
        
        visitPoint(currPoint, maze) # mark the current point as visited

        neighbors = getNeighbors(currPoint, maze) # get the neighbors of the current point

        for neighbor in neighbors:
            pointsVisited.append(neighbor) # add the neighbor to the stack


    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], end="")

    print(f"Iterations: {iterations}")


# This method will be use dijkstra to solve the maze, with the paramater the maze
#def dijkstra(maze: list[list[str]]):

            
# Now will run the code entirely

while True:
    p = input("\nWhich maze would you like to solve? (1-3) or type 0 to quit: ")

    if not p.isdigit():
        print("Please enter a valid number between 1-3 or 0 to quit.")
        continue

    p = int(p)

    if p < 0 or p > 3:
        print("Please enter a valid number between 1-3 or 0 to quit.")
        continue

    if p == 0:
        print("Quitting")
        break

    maze = readMaze(p)

    displayMaze(maze)

    print("\nFinding start point...\n")
    startPoint = findStart(maze)
    print(f"Start point found at: {startPoint}")

    print("\nSolving maze using depth first search algorithm...\n")
    dfs(maze)

    print("\nSolving maze using breadth first search algorithm...\n")
    maze = readMaze(p)
    bfs(maze)

