import math

from pygame.math import Vector2 as Vec2
from enum import IntFlag
from collections import namedtuple

from racingenv.physics.utils import sign, rotate_point, line_line_collision

Hitbox = namedtuple('Hitbox', ['tl', 'tr', 'br', 'bl', 'center'])


def map_action(index):
    if index == 0: return Action.FORWARD
    if index == 1: return Action.BACKWARD
    if index == 2: return Action.LEFT
    if index == 3: return Action.RIGHT
    if index == 4: return Action.FORWARD | Action.RIGHT
    if index == 5: return Action.FORWARD | Action.LEFT
    if index == 6: return Action.NONE


class Action(IntFlag):
    FORWARD = 0x01
    BACKWARD = 0x02,
    LEFT = 0x04,
    RIGHT = 0x08,
    NONE = 0x00


MAX_RAY_LENGTH = 500.0
NUM_RAYS = 8


class Car:
    def __init__(self,
                 image,
                 physics_settings,
                 num_rays=8,):
        self.acceleration = physics_settings["acceleration"]
        self.max_velocity = physics_settings["max_velocity"]
        self.max_lateral_velocity = physics_settings["max_lateral_velocity"]
        self.drift_threshold = physics_settings["drift_threshold"]
        self.drag = physics_settings["drag"]
        self.angular_velocity = physics_settings["angular_velocity"]
        self.lateral_drag = physics_settings["lateral_drag"]
        self.lateral_acceleration = physics_settings["lateral_acceleration"]

        self.position = Vec2(0, 0)
        self.dimensions = Vec2(image.get_size())
        self.direction = Vec2(0, -1)
        self.lateral_direction = self.direction.rotate(90.0)
        self.lateral_velocity = 0.0
        self.velocity = 0.0
        self.num_rays = num_rays
        self.alive = True
        self.image = image
        self.ray_points = []
        self.update_image = True
        self.rotated_image = self.image
        self.rect = self.image.get_rect()
        self.hitbox = Hitbox(Vec2(0, 0), Vec2(0, 0), Vec2(0, 0), Vec2(0, 0), Vec2(0, 0))
        self.__calculate_ray_points__()
        self.__calculate_hitbox__()

    def update(self, action):
        transformed_action = map_action(action)
        if transformed_action & Action.FORWARD != 0:
            self.velocity += self.acceleration
        elif transformed_action & Action.BACKWARD != 0:
            self.velocity -= self.acceleration
        else:
            drag = self.drag * -sign(self.velocity)

            if abs(drag) < abs(self.velocity):
                self.velocity += drag
            else:
                self.velocity = 0.0

        if self.velocity > self.max_velocity:
            self.velocity = self.max_velocity
        elif self.velocity < -self.max_velocity:
            self.velocity = -self.max_velocity

        if transformed_action & Action.LEFT != 0 and self.velocity != 0:
            self.direction = self.direction.rotate(-self.angular_velocity * sign(self.velocity))
            self.lateral_direction = self.direction.rotate(90.0)
            self.lateral_velocity += self.lateral_acceleration
            self.update_image = True
        elif transformed_action & Action.RIGHT != 0 and self.velocity != 0:
            self.direction = self.direction.rotate(self.angular_velocity * sign(self.velocity))
            self.lateral_direction = self.direction.rotate(-90.0)
            self.lateral_velocity += self.lateral_acceleration
            self.update_image = True
        else:
            lateral_drag = self.lateral_drag * -sign(self.lateral_velocity)

            if abs(lateral_drag) < abs(self.lateral_velocity):
                self.lateral_velocity += lateral_drag
            else:
                self.lateral_velocity = 0.0

        if self.lateral_velocity > self.max_lateral_velocity:
            self.lateral_velocity = self.max_lateral_velocity
        elif self.lateral_velocity < -self.max_lateral_velocity:
            self.lateral_velocity = -self.max_lateral_velocity

        if self.lateral_velocity < self.drift_threshold:
            self.lateral_direction = Vec2(0.0, 0.0)

        self.position += (self.direction * self.velocity + self.lateral_direction * self.lateral_velocity)

        self.__calculate_hitbox__()
        self.__calculate_ray_points__()

    def is_colliding(self, line_start, line_end):
        return line_line_collision(self.hitbox.tl, self.hitbox.tr, line_start, line_end) or \
            line_line_collision(self.hitbox.tr, self.hitbox.br, line_start, line_end) or \
            line_line_collision(self.hitbox.br, self.hitbox.bl, line_start, line_end) or \
            line_line_collision(self.hitbox.bl, self.hitbox.tl, line_start, line_end)

    def __calculate_hitbox__(self):
        angle = 2 * math.pi - math.radians(self.direction.angle_to(Vec2(0, 1)))

        # create a box with (0,0) as the center
        bl = Vec2(-self.dimensions.x / 2.0, self.dimensions.y / 2.0)
        br = Vec2(self.dimensions.x / 2.0, self.dimensions.y / 2.0)
        tl = Vec2(-self.dimensions.x / 2.0, -self.dimensions.y / 2.0)
        tr = Vec2(self.dimensions.x / 2.0, -self.dimensions.y / 2.0)

        # rotate the box around the origin
        bl = rotate_point(bl, angle)
        br = rotate_point(br, angle)
        tl = rotate_point(tl, angle)
        tr = rotate_point(tr, angle)

        # translate the box back to the right position
        bl += self.position + self.dimensions / 2.0
        br += self.position + self.dimensions / 2.0
        tl += self.position + self.dimensions / 2.0
        tr += self.position + self.dimensions / 2.0

        self.hitbox = Hitbox(tl, tr, br, bl, self.position + self.dimensions / 2.0)

    def __calculate_ray_points__(self):
        self.ray_points.clear()
        for i in range(0, self.num_rays):
            self.ray_points.append(
                self.hitbox.center + (self.direction.rotate(360 * i / self.num_rays).normalize()) * MAX_RAY_LENGTH
            )

    def update_physics_settings(self, physics_settings):
        self.acceleration = physics_settings["acceleration"]
        self.max_velocity = physics_settings["max_velocity"]
        self.max_lateral_velocity = physics_settings["max_lateral_velocity"]
        self.drift_threshold = physics_settings["drift_threshold"]
        self.drag = physics_settings["drag"]
        self.angular_velocity = physics_settings["angular_velocity"]
        self.lateral_drag = physics_settings["lateral_drag"]
        self.lateral_acceleration = physics_settings["lateral_acceleration"]
