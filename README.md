# Maze Solver: Pathfinding Algorithms

This Python project explores how different search algorithms navigate maze-like environments.

## Project Overview

I implemented and tested four pathfinding algorithms across six custom maze environments to compare how they find paths and how efficiently they explore their surroundings.

The project tracks metrics including path length, path cost, nodes explored, maximum frontier size, and runtime.

## Algorithms Implemented

- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Dijkstra's Algorithm
- A* Search

## Results

Maze 6 uses weighted terrain, demonstrating how the shortest path isn't necessarily the least costly.

| Algorithm | Path Length | Path Cost | Nodes Explored |
|---|---:|---:|---:|
| DFS | 27 | 162 | 28 |
| BFS | 27 | 162 | 81 |
| Dijkstra | 31 | 31 | 76 |
| A* | 31 | 31 | 42 |

Dijkstra and A* found lower-cost paths despite requiring more steps. A* also explored fewer nodes than Dijkstra in this maze.

## Technologies

- Python 3
- Standard libraries: `collections`, `heapq`, `time`

## Running the Program

Clone the repository and run:

```bash
git clone https://github.com/bladervnner/mazeSolver.git
cd mazeSolver
python main.py
```

Select a maze from the menu to compare the four algorithms. No additional packages are required.