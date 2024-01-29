import os

from pygame.math import Vector2 as Vec2

from racingenv.physics.car import Car, MAX_RAY_LENGTH
from racingenv.physics.track import Track
from racingenv.physics.utils import calculate_collision_point

from collections import namedtuple

from collision.collision import CollisionHandler

from racingenv import resource_dir

RayHit = namedtuple("RayHit", ["point", "distance", "wall"])


class Simulation:
    def __init__(self, resource_manager, physics_settings, num_rays):
        self.player = Car(resource_manager.load_sprite("Car.png", False), physics_settings)
        self.track = Track(resource_dir + 'Resources/Tracks/Hockenheim.xml', resource_manager)
        self.cp_id = 0
        self.laps = 0

        self.num_rays = num_rays
        self.ray_hits = [
            RayHit(Vec2(0.0), 0.0, None) for _ in range(self.num_rays)
        ]

        self.collisionHandler = CollisionHandler()

        temp = []
        for cp in self.track.checkpoints:
            temp.append(cp.start)
            temp.append(cp.end)

        self.collisionHandler.uploadData(self.track.inner_points, self.track.outer_points, temp, MAX_RAY_LENGTH)

    def reset(self):
        self.player.position = Vec2(300, 1500)
        self.player.direction = Vec2(0, -1).rotate(-20.0)
        self.player.lateral_direction = self.player.direction.rotate(90.0)
        self.player.update_image = True
        self.player.alive = True
        self.player.lateral_velocity = 0.0
        self.player.velocity = 0.0
        self.cp_id = 0
        self.laps = 0
        self.player.__calculate_hitbox__()

        for checkpoint in self.track.checkpoints:
            checkpoint.active = True

    def step(self, action):
        self.player.update(action)
        self.__col__()

    def __col__(self):
        collision_points, player_hit, checkpoint_hit = \
            self.collisionHandler.calculateCollisionPoints(self.player.ray_points,
                                                           self.player.hitbox.center,
                                                           [
                                                               self.player.hitbox.tl,
                                                               self.player.hitbox.tr,
                                                               self.player.hitbox.br,
                                                               self.player.hitbox.bl
                                                           ])

        self.ray_hits.clear()
        for point in collision_points:
            self.ray_hits.append(RayHit(Vec2(point[0], point[1]), point[2], None))

        if (player_hit):
            self.player.alive = False

        if (checkpoint_hit):
            self.track.checkpoints[self.cp_id].active = False
            self.cp_id += 1

            if self.cp_id == len(self.track.checkpoints):
                self.cp_id = 0
                self.laps += 1

                for cp in self.track.checkpoints:
                    cp.active = True

    def _update_collision(self):
        # only check player collision with walls the rays collided with
        # because there can be no collision with any other wall
        for hit in self.ray_hits:
            if hit.wall is not None and self.player.is_colliding(hit.wall.a, hit.wall.b):
                self.player.alive = False

    def _update_rays(self):
        self.ray_hits.clear()
        for ray_point in self.player.ray_points:
            point = ray_point
            distance = MAX_RAY_LENGTH
            obj = None

            for wall in self.track.walls:
                temp = calculate_collision_point(
                    self.player.hitbox.center, ray_point, wall.a, wall.b)

                if self.player.hitbox.center.distance_to(temp) < distance:
                    distance = self.player.hitbox.center.distance_to(temp)
                    point = temp
                    obj = wall

            self.ray_hits.append(RayHit(point, distance, obj))

    def _update_checkpoints(self):
        if self.cp_id < len(self.track.checkpoints):
            if self.player.is_colliding(self.track.checkpoints[self.cp_id].start, self.track.checkpoints[self.cp_id].end):
                self.track.checkpoints[self.cp_id].active = False
                self.cp_id += 1

        # if all checkpoints are inactive
        # check if the player is currently colliding with the last checkpoint (to prevent double activation)
        if self.cp_id == len(self.track.checkpoints):
            if self.player.is_colliding(self.track.checkpoints[self.cp_id - 1].start, self.track.checkpoints[self.cp_id - 1].end):
                for checkpoint in self.track.checkpoints:
                    checkpoint.active = True
