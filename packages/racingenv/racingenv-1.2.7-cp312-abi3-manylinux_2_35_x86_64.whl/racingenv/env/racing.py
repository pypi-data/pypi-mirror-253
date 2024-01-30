import logging
import copy

import pygame

from racingenv.renderer.resourcemanager import ResourceManager

import gymnasium as gym
import numpy as np
from gymnasium import spaces

from racingenv.physics.car import MAX_RAY_LENGTH
from racingenv.physics.simulation import Simulation
from racingenv.renderer.simulationrenderer import SimulationRenderer
from pygame.math import Vector2 as Vec2
from collections import namedtuple

from racingenv import resource_dir

RayHit = namedtuple("RayHit", ["point", "distance", "wall"])


class RacingEnv(gym.Env):
    metadata = {
        "render_modes": [
            "human",
            "agent",
            "rgb_array",
            "debug"
        ],
        "obs_types": [
            "pixels",
            "features"
        ],
        "render_fps": 60.0
    }

    def __init__(self, render_mode=None, obs_type=None, physics_settings=None, resolution=None, trunc_laps=2, normalize_images=False):
        if render_mode is not None and render_mode in self.metadata["render_modes"]:
            if render_mode == "debug":
                self.render_mode = "human"
                self.render_debug = True
            else:
                self.render_mode = render_mode
                self.render_debug = False
        else:
            # set "human" to be the default render mode
            self.render_mode = "human"
            self.render_debug = False

        if resolution is not None and self.render_mode == "human":
            self.width = resolution[0]
            self.height = resolution[1]
        elif obs_type == "features":
            self.width = 800
            self.height = 600
        elif obs_type == "pixels":
            self.width = 420
            self.height = 420

        self.reward = 0.0
        self.num_rays = 8
        self.cp_id = 0
        self.normalize_images = normalize_images

        # Initialise pygame for human render mode
        pygame.init()
        pygame.display.set_caption("RLRacer")

        self.clock = pygame.time.Clock()

        if physics_settings is None:
            self.physics_settings = {
                "max_velocity": 10.0,
                "acceleration": 0.4,
                "drag": 0.48,
                "max_lateral_velocity": 4.0,
                "lateral_acceleration": 0.4,
                "lateral_drag": 0.48,
                "angular_velocity": 6.0,
                "drift_threshold": 2.5
            }
        else:
            self.physics_settings = physics_settings

        pygame.display.init()

        if self.render_mode == "rgb_array":
            self.surface = pygame.surface.Surface(size=[self.width, self.height], flags=pygame.HWSURFACE | pygame.HWACCEL)
            self.resource_manager = ResourceManager(resource_dir + '/Resources/Textures/', False)
        else:
            self.surface = pygame.display.set_mode(size=[self.width, self.height], flags= pygame.DOUBLEBUF | pygame.HWSURFACE)
            self.resource_manager = ResourceManager(resource_dir + '/Resources/Textures/', True)

        self.renderer = SimulationRenderer(self.render_mode, self.width, self.height)
        self.simulation = Simulation(self.resource_manager, self.physics_settings, self.num_rays)

        self.lower_bound, self.upper_bound = Vec2(0.0, 0.0), Vec2(3360.0 + MAX_RAY_LENGTH, 1890.0 + MAX_RAY_LENGTH)

        if obs_type is None or obs_type not in self.metadata["obs_types"]:
            logging.warning("No obs type or illegal obs type specified, defaulting to features")

            self.obs_type = "features"
        else:
            self.obs_type = obs_type

        self.action_space = spaces.Discrete(6)
        if self.obs_type == "pixels":
            if self.normalize_images:
                self.observation_space = gym.spaces.Box(0, 1, shape=(84, 84, 3), dtype=np.float32)
            else:
                self.observation_space = gym.spaces.Box(0, 255, shape=(84, 84, 3), dtype=np.uint8)
        elif self.obs_type == "features":
            low = [
                0.0,  # x agent position
                0.0,  # y agent position
                -1.0,  # x direction
                -1.0,  # y direction
                0.0,  # distance to the next checkpoints inner bound
                -1.0,  # x direction to the next checkpoints inner bound
                -1.0,  # y direction to the next checkpoints inner bound
                0.0,  # distance to the next checkpoints outer bound
                -1.0,  # x direction to the next checkpoints outer bound
                -1.0,  # y direction to the next checkpoints outer bound
                -1.0,  # forward velocity
                -1.0,  # angular velocity
                -1.0  # lateral velocity
            ]
            for i in range(self.num_rays):
                low.extend(
                    [
                        0.0,  # distance to ray hit
                        -1.0,  # x position of hit point
                        -1.0,  # y position of hit point
                    ]
                )

            high = [
                1.0,  # x agent position
                1.0,  # y agent position
                1.0,  # x direction
                1.0,  # y direction
                1.0,  # distance to the next checkpoints inner bound
                1.0,  # x direction to the next checkpoints inner bound
                1.0,  # y direction to the next checkpoints inner bound
                1.0,  # distance to the next checkpoints outer bound
                1.0,  # x direction to the next checkpoints outer bound
                1.0,  # y direction to the next checkpoints outer bound
                1.0,  # forward velocity
                1.0,  # angular velocity
                1.0  # lateral velocity
            ]
            for i in range(self.num_rays):
                high.extend([
                    1.0,  # distance to ray hit
                    1.0,  # x position of hit point
                    1.0  # y position of hit point
                ]
                )

            self.observation_space = gym.spaces.Box(
                low=np.array(low),
                high=np.array(high),
                dtype=np.float_
            )

        self.is_moving = False
        self.trunc_laps = trunc_laps

    def reset(self, seed=None, options=None):
        self.simulation.reset()
        self.cp_id = 0
        self.is_moving = False

        for checkpoint in self.simulation.track.checkpoints:
            checkpoint.active = True

        return self._get_obs(), self._get_info()

    def step(self, action):
        self.simulation.step(action)
        self.renderer.camera.set(self.simulation.player.position.x - self.renderer.camera.viewport.width / 2.0,
                                 self.simulation.player.position.y - self.renderer.camera.viewport.height / 2.0)
        self._update_reward()

        if self.render_mode == "human" or self.render_mode == "agent" or self.obs_type == "pixels":
            self.render()

        return self._get_obs(), self.reward, not self.simulation.player.alive, self.simulation.laps == self.trunc_laps, self._get_info()

    def _update_reward(self):
        self.reward = -0.001

        if self.cp_id != self.simulation.cp_id:
            self.reward += 1.0
            self.cp_id = self.simulation.cp_id

        if not self.simulation.player.alive:
            self.reward -= -1.0

        if self.simulation.player.velocity == 0.0 and self.is_moving:
            self.reward -= 1.0
            self.is_moving = False

        if self.simulation.player.velocity != 0.0:
            self.is_moving = True

    def _get_obs(self):
        if self.obs_type == "pixels":
            transformed = pygame.transform.scale(self.surface, [84, 84])

            if self.normalize_images:
                return (pygame.surfarray.pixels3d(transformed)/255.0).astype(dtype=np.float32)
            else:
                return pygame.surfarray.pixels3d(transformed).astype(dtype=np.uint8)
        elif self.obs_type == "features":
            features = [
                self.simulation.player.hitbox.center.x/self.upper_bound.x,
                self.simulation.player.hitbox.center.y/self.upper_bound.y,
                self.simulation.player.direction.x,
                self.simulation.player.direction.y,
                np.clip(self.simulation.player.hitbox.center.distance_to(self.simulation.track.checkpoints[self.simulation.cp_id].start)/MAX_RAY_LENGTH, 0.0, 1.0),
                (self.simulation.track.checkpoints[self.simulation.cp_id].start - self.simulation.player.hitbox.center).normalize().x,
                (self.simulation.track.checkpoints[self.simulation.cp_id].start - self.simulation.player.hitbox.center).normalize().y,
                np.clip(self.simulation.player.hitbox.center.distance_to(self.simulation.track.checkpoints[self.simulation.cp_id].end) / MAX_RAY_LENGTH, 0.0, 1.0),
                (self.simulation.track.checkpoints[self.simulation.cp_id].end - self.simulation.player.hitbox.center).normalize().x,
                (self.simulation.track.checkpoints[self.simulation.cp_id].end - self.simulation.player.hitbox.center).normalize().y,
                self.simulation.player.velocity/self.simulation.player.max_velocity,
                self.simulation.player.angular_velocity/self.simulation.player.angular_velocity,
                self.simulation.player.lateral_velocity/self.simulation.player.max_lateral_velocity
            ]

            assert len(self.simulation.ray_hits) == self.num_rays
            for hit in self.simulation.ray_hits:
                features.extend(
                    [
                        hit.distance/MAX_RAY_LENGTH,  # distance to ray hit
                        hit.point.x/self.upper_bound.x,  # x position of hit point
                        hit.point.y/self.upper_bound.y,  # y position of hit point
                    ]
                )

            return np.array(features)

    def _get_info(self):
        return {}

    def render(self):
        self.renderer.render(self.simulation, self.render_debug, self.surface)

        # blit the frame onto the screen and lock the framerate
        if self.render_mode == "human" or self.render_mode == "agent":
            pygame.event.pump()

            self.clock.tick(self.metadata["render_fps"])
            pygame.display.flip()
        elif self.render_mode == "rgb_array":
            return pygame.surfarray.pixels3d(self.surface)

    def close(self):
        pygame.display.quit()
        pygame.quit()
