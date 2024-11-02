# booardgame
a navigation board game made using python.
Board Game Path Finder
This project is a Python-based solution for a board game where a player finds the shortest path across a grid with obstacles, using specified movement rules.

Problem Description
Ankitha and her friend Akhil play a grid-based game. Akhil is given an M x N grid where each cell contains either 0 (open) or 1 (blocked). Given specific source and destination coordinates, he must find the shortest path to reach the destination while only moving to cells containing 0. Movement is governed by a move rule that specifies how many steps to take in four possible directions (forward, backward, left, and right).

Goal: Calculate the minimum number of moves required to reach the destination, or indicate if it's impossible to reach.

Rules of Movement
The move rule specifies an (dx, dy) pair of integers that govern how far Akhil can move in four directions:

Forward: (x + dx, y + dy)
Right: Rotate 90 degrees clockwise: (x + dy, y - dx)
Left: Rotate 90 degrees counterclockwise: (x - dy, y + dx)
Backward: Rotate 180 degrees: (x - dx, y - dy)
Input Format
Grid dimensions as M N (number of rows and columns)
M lines for the grid where each cell contains 0 (open) or 1 (blocked)
Source coordinates as x y
Destination coordinates as x y
Move rule as dx dy
Example Input
6 6
0 1 0 0 0 0
0 0 0 0 0 1
0 1 0 0 0 0
1 1 0 0 0 1
0 0 0 0 0 0
1 1 0 0 1 0
1 0
5 3
1 2
Expectd output
Minimum moves required to reach the destination: 3
How to Run
Prerequisites
Python 3.x

