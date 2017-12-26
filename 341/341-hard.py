#!/usr/bin/python
# 341-hard Finding a Map Subsection
"""
* The entire path must be contained within the output area.
* The smaller area must not extend beyond the edge of the larger map.
* Because the viewing terminal display is square, the output bounds must be
  square.
* If possible, add a 30 pixel border around the path, so the path doesn't go
  right to the edge of the screen. If a point is within 30 pixels of the edge,
  go up to the edge.
* The path should be centered within the smaller bounds, when possible.
* NOTE: These requirements are listed in order of importance.
The output being square is more important than the 30 pixel border, etc.
This means there may be cases where 30px border is not possible (the path is
very close to an edge of the map), or where it's not possible to be centered
(path is in a corner of the map), etc.
"""


def getMap(mapSize, pathPoints):
    """ takes map size, and set of coordinates. returns a bounding box.
    eg: getmap(2000, [(1000, 1500), (1200, 1500),(1400,1600),(1600,1800)])
          -> something like (970, 1320), 660
        first being the lower left corner coordinate, second being the size
        of the square bounding box."""

    x_sorted = sorted(pathPoints)
    smallest_x = x_sorted[0][0]
    biggest_x = x_sorted[-1][0]

    y_sorted = sorted(pathPoints, key=lambda n: n[1])
    smallest_y = y_sorted[0][1]
    biggest_y = y_sorted[-1][1]

    bot_lt = (smallest_x, smallest_y)

    width = biggest_x - smallest_x
    height = biggest_y - smallest_y

    # square up our dimensions.
    if width < height:
        width = height



# our test cases, given for the challenge.
print(
    getMap(2000, [(600, 600), (700, 1200)]) == [(320, 570), 660],
    getMap(2000, [(300, 300), (1300, 300)]) == [(270, 0), 1060],
    getMap(2000,
           [(825, 820),
            (840, 830),
            (830, 865), (835, 900)]) == [(763, 790), 140],
    )
