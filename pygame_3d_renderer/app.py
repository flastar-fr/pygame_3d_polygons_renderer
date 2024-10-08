import pygame

from manager_3d import Manager3d


class App:
    def __init__(self, game_screen: pygame.display):
        pygame.init()
        self.screen: pygame.display = game_screen
        self.clock = pygame.time.Clock()
        self.manager_3d = Manager3d()
        self.show_hided = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    self.manager_3d.change_structure("cube")
                if event.key == pygame.K_p:
                    self.manager_3d.change_structure("pyramide")
                if event.key == pygame.K_l:
                    self.manager_3d.change_structure("plan")
                if event.key == pygame.K_s:
                    self.show_hided = not self.show_hided

    def draw_vertices(self):
        width, height = self.screen.get_size()
        for key, vertex in self.manager_3d.vertices.items():
            if self.manager_3d.is_point_visible(key) or self.show_hided:
                x, y = self.manager_3d.get_point_2d_position(vertex)
                x, y = x + width // 2, y + height // 2
                pygame.draw.circle(self.screen, pygame.Color(255, 255, 255), (x, y), 5)

    def draw_edges(self):
        vertex_table = self.manager_3d.vertices
        width, height = self.screen.get_size()
        for edge in self.manager_3d.edges:
            if self.manager_3d.is_edge_visible(edge) or self.show_hided:
                x1, y1 = self.manager_3d.get_point_2d_position(vertex_table[edge[0]])
                x2, y2 = self.manager_3d.get_point_2d_position(vertex_table[edge[1]])

                x1, y1 = x1 + width // 2, y1 + height // 2
                x2, y2 = x2 + width // 2, y2 + height // 2

                pygame.draw.line(self.screen, pygame.Color(255, 255, 255), (x1, y1), (x2, y2))

    def run(self):
        self.screen.fill("black")

        self.handle_events()
        self.draw_vertices()
        self.draw_edges()

        self.manager_3d.rotate_points(0, 1, -1)

        pygame.display.update()
        self.clock.tick(60)
