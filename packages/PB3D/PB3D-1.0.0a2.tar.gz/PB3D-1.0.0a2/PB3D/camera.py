from OpenGL.GLU import gluLookAt
from PB3D.math import RGB
from PB3D.math.vector import BaseVec3
from PB3D.entity import Entity
from PB3D.event import button_dict

class Camera(Entity):
    """
    *** caution! This is not fully functional!***
    This is the class responsible for the camera in PB3D
    """
    def __init__(self, color: RGB, file_path="cube", position: BaseVec3 = BaseVec3(0, 0, 0)):
        super().__init__(
            file_path=file_path,
            color=color,
            position=position
        )

    def update(self, direction, speed):
        if direction == button_dict["d"]:
            self.position.x += speed
        elif direction == button_dict["a"]:
            self.position.x -= speed
        elif direction == button_dict["w"]:
            self.position.z -= speed
        elif direction == button_dict["s"]:
            self.position.z += speed
        self.set_view()

    def set_view(self):
        gluLookAt(self.position.x, self.position.y, self.position.z, 0, 0, 0, 0, 1, 0)