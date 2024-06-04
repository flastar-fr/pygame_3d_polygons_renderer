from math import cos, sin

import numpy as np

from pygame import Vector3

from structures import structures


scale_factor = 200


class Manager3d:
    def __init__(self):
        self.vertices = None
        self.edges = None
        self.faces = None
        self.change_structure("cube")
        self.camera_pos = Vector3(0, 0, -1)
        self.focal_lenght = 500

    def change_structure(self, structure_name: str):
        self.vertices = structures[structure_name]["vertices"]
        self.edges = structures[structure_name]["edges"]
        self.faces = structures[structure_name]["faces"]

    def get_center(self):
        center = Vector3()
        for vertex in self.vertices.values():
            center += vertex
        center /= len(self.vertices)
        return center

    def get_point_2d_position(self, vertex: Vector3):
        transformed_vertex = vertex - self.camera_pos

        x = ((self.focal_lenght * (transformed_vertex.x * scale_factor)) /
             (self.focal_lenght + (transformed_vertex.z * scale_factor)))
        y = ((self.focal_lenght * (transformed_vertex.y * scale_factor)) /
             (self.focal_lenght + (transformed_vertex.z * scale_factor)))

        return x, y

    def rotate_points(self, x_angle, y_angle, z_angle):
        center = self.get_center()
        x_angle, y_angle, z_angle = np.radians(x_angle), np.radians(y_angle), np.radians(z_angle)

        r_x = np.array([[1, 0, 0],
                        [0, cos(x_angle), -sin(x_angle)],
                        [0, sin(x_angle), cos(x_angle)]])
        r_y = np.array([[cos(y_angle), 0, sin(y_angle)],
                        [0, 1, 0],
                        [-sin(y_angle), 0, cos(y_angle)]])
        r_z = np.array([[cos(z_angle), -sin(z_angle), 0],
                        [sin(z_angle), cos(z_angle), 0],
                        [0, 0, 1]])

        rotation_matrix = r_x @ r_y @ r_z

        for key, vertex in self.vertices.items():
            coordinates_matrix = np.array([vertex.x - center.x, vertex.y - center.y, vertex.z - center.z])
            rotated_coordinates = rotation_matrix @ coordinates_matrix
            self.vertices[key] = Vector3(float(rotated_coordinates[0]),
                                         float(rotated_coordinates[1]),
                                         float(rotated_coordinates[2]))
