import pygame
from pygame.math import Vector2 as Vec2

from racingenv.renderer.resourcemanager import rotate_image


class CarRenderer:
    def render(self, surface, camera, car):
        if car.update_image:
            car.rotated_image, car.rect = rotate_image(car.image,
                                                       car.direction.angle_to(Vec2(0, 1)), car.position,True)
            car.update_image = False
        else:
            car.rect = car.rotated_image.get_rect(center=car.image.get_rect(topleft=car.position).center)

        surface.blit(car.rotated_image, camera.translate_rect(car.rect))

    def render_debug(self, surface, camera, car):
        pygame.draw.line(surface, [255, 128, 0],
                         camera.translate_point(car.hitbox.bl), camera.translate_point(car.hitbox.br))
        pygame.draw.line(surface, [255, 128, 0],
                         camera.translate_point(car.hitbox.br), camera.translate_point(car.hitbox.tr))
        pygame.draw.line(surface, [255, 128, 0],
                         camera.translate_point(car.hitbox.tr), camera.translate_point(car.hitbox.tl))
        pygame.draw.line(surface, [255, 128, 0],
                         camera.translate_point(car.hitbox.tl), camera.translate_point(car.hitbox.bl))

        for point in car.ray_points:
            pygame.draw.line(surface, [0, 0, 255],
                             camera.translate_point(car.hitbox.center),
                             camera.translate_point(point))