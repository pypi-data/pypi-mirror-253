import pygame
from pygame.math import Vector2 as Vec2


class TrackRenderer:
    def render_debug(self, color, surface, track, camera, enable_aa):
        if enable_aa:
            pygame.draw.aalines(surface, color, True, camera.translate_points(track.outer_points))
            pygame.draw.aalines(surface, color, True, camera.translate_points(track.inner_points))
        else:
            pygame.draw.lines(surface, color, True, camera.translate_points(track.outer_points))
            pygame.draw.lines(surface, color, True, camera.translate_points(track.inner_points))

        for checkpoint in track.checkpoints:
            self.render_checkpoint(surface, camera, enable_aa, checkpoint)

    def render(self, surface, camera, track):
        surface.blit(track.image, camera.translate_point(Vec2(0.0, 0.0)))

    def render_checkpoint(self, surface, camera, enable_aa, checkpoint):
        if checkpoint.active:
            color = [255, 128, 0]
        else:
            color = [0, 255, 128]

        if enable_aa:
            pygame.draw.aaline(surface, color,
                               camera.translate_point(checkpoint.start), camera.translate_point(checkpoint.end))
        else:
            pygame.draw.line(surface, color,
                             camera.translate_point(checkpoint.start), camera.translate_point(checkpoint.end))
