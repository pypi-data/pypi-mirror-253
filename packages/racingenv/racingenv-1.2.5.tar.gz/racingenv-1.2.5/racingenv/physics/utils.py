from pygame.math import Vector2 as Vec2
from math import copysign, cos, sin


def sign(x):
    return copysign(1, x)


def clamp(min, max, val):
    if val > max:
        return max
    elif val < min:
        return min

    return val


def rotate_point(point, angle):
    return Vec2(point.x * cos(angle) - point.y * sin(angle),
                point.x * sin(angle) + point.y * cos(angle))


def line_line_collision(a1, a2, b1, b2):
    uA, uB = calculate_collision_factor(a1, a2, b1, b2)
    return 0 <= uA <= 1 and 0 <= uB <= 1


def calculate_collision_factor(a1, a2, b1, b2):
    # Exclude parallel lines
    if ((b2.y - b1.y) * (a2.x - a1.x) - (b2.x - b1.x) * (a2.y - a1.y)) == 0 or (
            (b2.y - b1.y) * (a2.x - a1.x) - (b2.x - b1.x) * (a2.y - a1.y)) == 0:
        return float('inf'), float('inf')

    uA = ((b2.x - b1.x) * (a1.y - b1.y) - (b2.y - b1.y) * (a1.x - b1.x)) / \
         ((b2.y - b1.y) * (a2.x - a1.x) - (b2.x - b1.x) * (a2.y - a1.y))
    uB = ((a2.x - a1.x) * (a1.y - b1.y) - (a2.y - a1.y) * (a1.x - b1.x)) / \
         ((b2.y - b1.y) * (a2.x - a1.x) - (b2.x - b1.x) * (a2.y - a1.y))

    return uA, uB


def calculate_collision_point(a1, a2, b1, b2):
    uA, uB = calculate_collision_factor(a1, a2, b1, b2)

    if 0 <= uA <= 1 and 0 <= uB <= 1:
        return Vec2(a1.x + (uA * (a2.x - a1.x)), a1.y + (uA * (a2.y - a1.y)))

    return Vec2(float('inf'), float('inf'))
