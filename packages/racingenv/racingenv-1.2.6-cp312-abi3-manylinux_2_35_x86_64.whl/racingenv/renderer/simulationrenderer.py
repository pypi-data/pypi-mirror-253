import pygame
from pygame.math import Vector2 as Vec2

from racingenv.renderer.camera import Camera
from racingenv.renderer.carrenderer import CarRenderer
from racingenv.renderer.trackrenderer import TrackRenderer


class SimulationRenderer:
    def __init__(self, render_mode, width, height):
        self.font = pygame.font.SysFont('arial', 24)
        self.camera = Camera(width, height)
        self.render_mode = render_mode
        self.car_renderer = CarRenderer()
        self.track_renderer = TrackRenderer()

    def render(self, simulation, render_debug, surface):
        surface.fill(pygame.color.Color(0, 0, 0, 255))

        if self.render_mode == "human" or self.render_mode == "rgb_array":
            self._render_human(simulation, surface)

            if render_debug:
                self._render_debug(simulation, surface)
        elif self.render_mode == "agent":
            self._render_agent(simulation, surface)

    def _render_human(self, simulation, surface):
        self.track_renderer.render(surface, self.camera, simulation.track)
        self.car_renderer.render(surface, self.camera, simulation.player)

    def _render_agent(self, simulation, surface):
        for hit in simulation.ray_hits:
            pygame.draw.circle(surface, [0, 0, 255], self.camera.translate_point(hit.point), radius=6.0)

        for point in simulation.player.ray_points:
            pygame.draw.line(surface, [0, 0, 255],
                             self.camera.translate_point(simulation.player.hitbox.center),
                             self.camera.translate_point(point))

        pygame.draw.line(
            surface, [255, 0, 0],
            self.camera.translate_point(simulation.player.hitbox.center),
            self.camera.translate_point(simulation.player.hitbox.center +
                                        simulation.player.direction *
                                        simulation.player.velocity * 100),
            width=2)

        pygame.draw.line(
            surface, [255, 0, 0],
            self.camera.translate_point(simulation.player.hitbox.center),
            self.camera.translate_point(simulation.player.hitbox.center +
                                        simulation.player.lateral_direction *
                                        simulation.player.lateral_velocity * 50),
            width=2)

        pygame.draw.line(surface, [255, 0, 0],
                         self.camera.translate_point(simulation.player.hitbox.center),
                         self.camera.translate_point(simulation.track.checkpoints[simulation.cp_id].start),
                         width=2)

        pygame.draw.line(surface, [255, 0, 0],
                         self.camera.translate_point(simulation.player.hitbox.center),
                         self.camera.translate_point(simulation.track.checkpoints[simulation.cp_id].end),
                         width=2)

    def _render_debug(self, simulation, surface):
        for hit in simulation.ray_hits:
            pygame.draw.circle(surface, [0, 0, 255], self.camera.translate_point(hit.point), radius=6.0)

        self.track_renderer.render_debug((255, 0, 0), surface, simulation.track, self.camera, True)
        self.car_renderer.render_debug(surface, self.camera, simulation.player)

        pygame.draw.line(surface, [255, 128, 0],
                         self.camera.translate_point(Vec2(0.0, 0.0)), self.camera.translate_point(Vec2(3500.0, 0.0)),
                         width=2)
        pygame.draw.line(surface, [255, 128, 0],
                         self.camera.translate_point(Vec2(0.0, 500.0)),
                         self.camera.translate_point(Vec2(3500.0, 500.0)), width=2)
        pygame.draw.line(surface, [255, 128, 0],
                         self.camera.translate_point(Vec2(0.0, 1000.0)),
                         self.camera.translate_point(Vec2(3500.0, 1000.0)), width=2)
        pygame.draw.line(surface, [255, 128, 0],
                         self.camera.translate_point(Vec2(0.0, 1500.0)),
                         self.camera.translate_point(Vec2(3500.0, 1500.0)), width=2)
        pygame.draw.line(surface, [255, 128, 0],
                         self.camera.translate_point(Vec2(0.0, 2000.0)),
                         self.camera.translate_point(Vec2(3500.0, 2000.0)), width=2)
        pygame.draw.line(surface, [255, 128, 0],
                         self.camera.translate_point(Vec2(500.0, 0.0)),
                         self.camera.translate_point(Vec2(500.0, 2000.0)), width=2)
        pygame.draw.line(surface, [255, 128, 0],
                         self.camera.translate_point(Vec2(1000.0, 0.0)),
                         self.camera.translate_point(Vec2(1000.0, 2000.0)), width=2)
        pygame.draw.line(surface, [255, 128, 0],
                         self.camera.translate_point(Vec2(1500.0, 0.0)),
                         self.camera.translate_point(Vec2(1500.0, 2000.0)), width=2)
        pygame.draw.line(surface, [255, 128, 0],
                         self.camera.translate_point(Vec2(2000.0, 0.0)),
                         self.camera.translate_point(Vec2(2000.0, 2000.0)), width=2)
