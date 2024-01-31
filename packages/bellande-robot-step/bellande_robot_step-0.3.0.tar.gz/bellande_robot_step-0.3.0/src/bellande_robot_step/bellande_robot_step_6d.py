#!/usr/bin/env python3

import numpy as np

class Node6D:
    def __init__(self, x, y, z, w, v, u, parent=None):
        self.coord = (x, y, z, w, v, u)
        self.parent = parent

    @property
    def x(self):
        return self.coord[0]

    @property
    def y(self):
        return self.coord[1]

    @property
    def z(self):
        return self.coord[2]

    @property
    def w(self):
        return self.coord[3]

    @property
    def v(self):
        return self.coord[4]

    @property
    def u(self):
        return self.coord[5]



def bellande_step_6d(node0, node1, limit=75):
    delta_x = node1.x - node0.x
    delta_y = node1.y - node0.y
    delta_z = node1.z - node0.z
    delta_w = node1.w - node0.w
    delta_v = node1.v - node0.v
    delta_u = node1.u - node0.u
    
    dist = np.sqrt(delta_x ** 2 + delta_y ** 2 + delta_z ** 2 + delta_w ** 2 + delta_v ** 2 + delta_u ** 2)
    
    if dist < limit:
        return node1
    
    ratio = limit / dist
    step_x = node0.x + delta_x * ratio
    step_y = node0.y + delta_y * ratio
    step_z = node0.z + delta_z * ratio
    step_w = node0.w + delta_w * ratio
    step_v = node0.v + delta_v * ratio
    step_u = node0.u + delta_u * ratio
    
    return Node6D(step_x, step_y, step_z, step_w, step_v, step_u)
