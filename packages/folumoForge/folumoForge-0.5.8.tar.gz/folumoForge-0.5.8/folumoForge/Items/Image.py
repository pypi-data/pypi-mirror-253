import pygame
from .. import itemBase, Screen


class Image(itemBase):
    def __init__(self, screen: Screen, path, xy, wh=None):
        super().__init__("Image")
        self.screen = screen
        screen.Items.append(self)
        self.xy = screen.root.relative(xy[0], xy[1])
        self.path = path

        self.img = pygame.image.load(path)
        if wh:
            self.wh = screen.root.relative(wh[0], wh[1])
            self.img = pygame.transform.scale(self.img, self.wh)

        self.rect = self.img.get_rect()

    def config(self, path=None, xy=None, wh=None):
        if xy:
            self.xy = xy

        if path:
            self.path = path
            self.img = pygame.image.load(path)
            if self.wh:
                self.img = pygame.transform.scale(self.img, self.wh)

        if wh:
            self.wh = wh
            self.img = pygame.transform.scale(self.img, wh)

        self.rect = self.img.get_rect()

    def update(self):
        self.rect = self.screen.root.MainRoot.blit(self.img, self.xy)