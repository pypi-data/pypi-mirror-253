import pygame
from pygame.math import Vector2 as Vec2


class Camera:
    def __init__(self, width, height):
        self.canvas = pygame.Surface([width, height])
        self.viewport = pygame.Rect(0.0, 0.0, width, height)

    def translate_rect(self, rect):
        return rect.move(-self.viewport.left, -self.viewport.top)

    def translate_point(self, point):
        return Vec2(point.x - self.viewport.left, point.y - self.viewport.top)

    def translate_points(self, points):
        result = []
        for point in points:
            result.append(self.translate_point(point))

        return result

    def move(self, x, y):
        self.viewport.move_ip(x, y)

    def set(self, x, y):
        self.viewport.update(x, y, self.viewport.width, self.viewport.height)
