from math import cos, sin

import numpy as np

from pygame import Vector3, Vector2

from polygons import polygons


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
        self.vertices = polygons[structure_name]["vertices"]
        self.edges = polygons[structure_name]["edges"]
        self.faces = polygons[structure_name]["faces"]

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

    # noinspection PyUnusedLocal,PyUnreachableCode
    def _get_z_point_in_face(self, point: Vector2, face: str) -> tuple[float, float, float, float]:
        # cartesian equation of a plan : ax + by + cz + d = 0
        p1, p2, p3 = self.vertices[face[0]], self.vertices[face[1]], self.vertices[face[2]]

        v1 = p2 - p1
        v2 = p3 - p1

        normal_vector = np.cross(v1, v2)   # values : a, b, c
        a, b, c = normal_vector

        d = -np.dot(normal_vector, p1)  # value : d

        return a, b, c, d

    def is_point_not_visible(self, vertex_name: str) -> bool:
        for face in self.faces:
            if vertex_name not in face:
                vertex = self.vertices[vertex_name]
                a, b, c, d = self._get_z_point_in_face(vertex.xy, face)

                if c == 0:
                    return False

                z_face_point = -(a * vertex.x + b * vertex.y + d) / c

                if z_face_point >= vertex.z:
                    return False

        return True

    def is_edge_not_visible(self, edge: str) -> bool:
        return self.is_point_not_visible(edge[0]) or self.is_point_not_visible(edge[1])

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
