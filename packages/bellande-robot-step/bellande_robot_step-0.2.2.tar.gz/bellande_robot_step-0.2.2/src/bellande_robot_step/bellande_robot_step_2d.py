#!/usr/bin/env python3

import numpy as np

class Node2D:
    def __init__(self, x, y, parent=None):
        self.coord = (x, y)
        self.parent = parent

    @property
    def x(self):
        return self.coord[0]

    @property
    def y(self):
        return self.coord[1]


def bellande_step_2d(node0, node1, limit=75):
    delta_x = node1.x - node0.x
    delta_y = node1.y - node0.y
    dist = np.sqrt(delta_x ** 2 + delta_y ** 2)

    if dist < limit:
        return node1

    ratio = limit / dist
    step_x = node0.x + delta_x * ratio
    step_y = node0.y + delta_y * ratio

    return Node2D(step_x, step_y)
