#!/usr/bin/python

maze = []
print("Input your maze:")
while True:
    try:
        maze.append(input())
    except EOFError:  # more pythonic way? there has to be.
        break

for line in maze:
    print(line)

orders = input('Input orders for the robot:')


class robot(object):
    def __init__(self, maze, orders=None):
        self.maze = maze
        self.orders = orders
        self.activestatus = False
        self.location = None
        for row in maze:
            if row.index('M'):
                # standard (x, y) positioning.
                if self.location is not None:
                    raise ValueError('maze supplied has too many robots M!')
                self.location = (row.index('M'), row)
        if self.location is None:
            raise ValueError('maze supplied to robot has no robot M')

    def move(self, order):
        if order not in "NSEOI-":
            raise ValueError('Invalid command for robot:' + order)
        if order == 'I':
            self.activestatus = True
        if order == '-':
            self.activestatus = False
        if self.activestatus:
            if order == 'N':
                pass
            if order == 'S':
                pass
            if order == 'E':
                pass
            if order == 'O':  # west.
                pass
