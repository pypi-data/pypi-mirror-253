import pygame

from .. import itemBase, Screen


class Arc(itemBase):
    def __init__(self, screen: Screen, xy=(0, 0), wh=(50, 50), color="white", start_angle=0, stop_angle=180, width=1):
        super().__init__("Arc")
        self.rectE = pygame.Rect(screen.root.relative(xy[0], xy[1]), screen.root.relative(wh[0], wh[1]))
        self.rect = pygame.Rect((0, 0), (0, 0))

        self.xy = xy
        self.wh = wh
        self.color = color
        self.start_angle = start_angle
        self.stop_angle = stop_angle
        self.width = width

        self.screen = screen
        screen.Items.append(self)

    def config(self, xy, wh, color, start_angle, stop_angle, width=1):
        self.rectE = pygame.Rect(xy, wh)
        self.xy = self.screen.root.relative(xy[0], xy[1])
        self.wh = self.screen.root.relative(wh[0], wh[1])
        self.color = color
        self.start_angle = start_angle
        self.stop_angle = stop_angle
        self.width = width

    def update(self):
        self.rect = pygame.draw.arc(self.screen.root.MainRoot, self.color, self.rectE,
                                    self.start_angle,
                                    self.stop_angle,
                                    self.width)

        return self.rect
