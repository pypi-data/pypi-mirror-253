from racingenv.physics.utils import calculate_collision_point
from racingenv.physics.car import MAX_RAY_LENGTH

from collections import namedtuple
RayHit = namedtuple("RayHit", ["point", "distance", "wall"])


class NativeCollisionHandler:
    def update(self, simulation):
        self._update_rays(simulation)
        self._update_collision(simulation)
        self._update_checkpoints(simulation)

    def _update_collision(self, simulation):
        # only check player collision with walls the rays collided with
        # because there can be no collision with any other wall
        for hit in simulation.ray_hits:
            if hit.wall is not None and simulation.player.is_colliding(hit.wall.a, hit.wall.b):
                simulation.player.alive = False

    def _update_rays(self, simulation):
        simulation.ray_hits.clear()
        for ray_point in simulation.player.ray_points:
            point = ray_point
            distance = MAX_RAY_LENGTH
            obj = None

            for wall in simulation.track.walls:
                temp = calculate_collision_point(
                    simulation.player.hitbox.center, ray_point, wall.a, wall.b)

                if simulation.player.hitbox.center.distance_to(temp) < distance:
                    distance = simulation.player.hitbox.center.distance_to(temp)
                    point = temp
                    obj = wall

            simulation.ray_hits.append(RayHit(point, distance, obj))

    def _update_checkpoints(self, simulation):
        if simulation.cp_id < len(simulation.track.checkpoints):
            if simulation.player.is_colliding(simulation.track.checkpoints[simulation.cp_id].start, simulation.track.checkpoints[simulation.cp_id].end):
                simulation.track.checkpoints[simulation.cp_id].active = False
                simulation.cp_id += 1

        # if all checkpoints are inactive
        # check if the player is currently colliding with the last checkpoint (to prevent double activation)
        if simulation.cp_id == len(simulation.track.checkpoints):
            if simulation.player.is_colliding(simulation.track.checkpoints[simulation.cp_id - 1].start, simulation.track.checkpoints[simulation.cp_id - 1].end):
                for checkpoint in simulation.track.checkpoints:
                    checkpoint.active = True
