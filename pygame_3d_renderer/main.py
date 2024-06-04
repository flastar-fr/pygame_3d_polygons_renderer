import pygame

from app import App


width, height = 800, 500
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3d Renderer")

app = App(game_screen)

while True:
    app.run()
