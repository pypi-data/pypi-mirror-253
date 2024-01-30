import numpy as np

from xml.etree import ElementTree
from pygame.math import Vector2 as Vec2
from collections import namedtuple

Wall = namedtuple('Wall', ['a', 'b'])


class Checkpoint:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.active = True


class Track:
    def __init__(self, map_file, resource_manager):
        self.walls = []
        self.inner_points = []
        self.outer_points = []
        self.checkpoints = []
        self.image = None

        tree = ElementTree.parse(map_file)

        root = tree.getroot()
        self.image = resource_manager.load_sprite(root.attrib['texture'], False)

        buffer = [
            root.attrib['outer'],
            root.attrib['inner'],
            root.attrib['checkpoints_inner'],
            root.attrib['checkpoints_outer']
        ]

        temp = []
        for token in buffer[0].split(' '):
            temp.append(float(token))

        for x, y in zip(*[iter(temp)] * 2):
            self.outer_points.append(Vec2(x, y))

        temp.clear()

        for token in buffer[1].split(' '):
            temp.append(float(token))

        for x, y in zip(*[iter(temp)] * 2):
            self.inner_points.append(Vec2(x, y))

        temp.clear()

        for i, point in enumerate(self.outer_points):
            if i < len(self.outer_points) - 1:
                self.walls.append(Wall(self.outer_points[i], self.outer_points[i + 1]))

        self.walls.append(Wall(self.outer_points[0], self.outer_points[-1]))

        for i, point in enumerate(self.inner_points):
            if i < len(self.inner_points) - 1:
                self.walls.append(Wall(self.inner_points[i], self.inner_points[i + 1]))

        self.walls.append(Wall(self.inner_points[0], self.inner_points[-1]))

        temp.clear()

        for token in buffer[2].split(' '):
            temp.append(float(token))

        for x, y in zip(*[iter(temp)] * 2):
            self.checkpoints.append(Checkpoint(Vec2(x, y), Vec2(0.0, 0.0)))

        temp.clear()

        for token in buffer[3].split(' '):
            temp.append(float(token))

        for i, point in enumerate(zip(*[iter(temp)] * 2)):
            self.checkpoints[i].end = Vec2(point[0], point[1])

    def get_bounds(self):
        low, high = Vec2(np.inf, np.inf), Vec2(-np.inf, -np.inf)

        for point in self.inner_points:
            if point.x < low.x:
                low.x = point.x
            elif point.x > high.x:
                high.x = point.x

            if point.y < low.y:
                low.y = point.y
            elif point.y > high.y:
                high.y = point.y

        for point in self.outer_points:
            if point.x < low.x:
                low.x = point.x
            elif point.x > high.x:
                high.x = point.x

            if point.y < low.y:
                low.y = point.y
            elif point.y > high.y:
                high.y = point.y

        return low, high
