import pygame
from pygame.locals import *
from OpenGL.GL import glTranslatef, glClear, glRotatef, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, glOrtho
from OpenGL.GLU import gluPerspective

def init(size: tuple[int, int]):
    pygame.init()
    pygame.display.set_mode(size, DOUBLEBUF | OPENGL)
    gluPerspective(45, (size[0] / size[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def init_2d(size: tuple[int, int]):
    pygame.init()
    pygame.display.set_mode(size, DOUBLEBUF | OPENGL)
    glOrtho(0, size[0], size[1], 0, -1, 1)

def update():
    pygame.display.flip()

def clean():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def turn(angle, x, y, z):
    glRotatef(angle, x, y, z)


def loop(func1=None, func2=None):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if func2 != None:
                func2()

        if func1 != None:
            func1()

Event = pygame.event.Event