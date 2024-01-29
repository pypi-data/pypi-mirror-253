from OpenGL.GLU import *
from PB3D.math.vector import Vec4
from PB3D.event import button_dict
import math

class Camera:
    """
    *** caution! This is not fully functional!***
    This is the class responsible for the camera in PB3D
    """
    def __init__(self, position: Vec4 = Vec4(0, 0, 0, 0)):
        self.position = position
        self.pitch = 0
        self.yaw = 0
        self.mouse_sensitivity = 0.1
        self.move_speed = 0.1
        self.front = Vec4(0, 0, -1, 0)
        self.up = Vec4(0, 1, 0, 0)

    def update(self, direction, speed):
        if direction == button_dict["w"]:
            self.position += self.front * speed
        elif direction == button_dict["s"]:
            self.position -= self.front * speed

        self.update_vectors()

    def rotate(self, dx, dy):
        dx *= self.mouse_sensitivity
        dy *= self.mouse_sensitivity

        self.yaw += dx
        self.pitch -= dy

        self.update_vectors()

    def update_vectors(self):
        self.front.x = math.cos(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))
        self.front.y = math.sin(math.radians(self.pitch))
        self.front.z = math.sin(math.radians(self.yaw)) * math.cos(math.radians(self.pitch))
        self.front = self.front.normalize()
        self.set_view()

    def set_view(self):
        center = self.position + self.front
        gluLookAt(self.position.x, self.position.y, self.position.z,
                  center.x, center.y, center.z,
                  self.up.x, self.up.y, self.up.z)
