import pygame as pg
import sys
import numpy as np
from typing import Protocol

class SimulationObject(Protocol):

    position: np.array([float])
    velocity: np.array([float])
    mass: float


    """Object interface with the game engine class."""
    def update(self):
        ...
        '''Update the simulation objects position'''

    def paint(self, canvas: pg.display):
        ...
        '''Paints the simulation object'''

    def update_velocity(self, objects):
        ...
    '''Update the velocity of the simulation objects'''

    def compute_forces(self, other):
        ...
    '''Compute relevant forces acting upon the object'''


class Engine:
    """Pygame Engine Object for handling game object rendering.
    How each object is rendered is delegated to the individual object via protocol and interfaced through
    the simulation object interface."""
    def __init__(self, title: str, background: tuple[int, ...] = (0,0,0), width: int = 500, height: int = 500, timestep=60):

        self.width = width
        self.height = height
        self.background = background
        self.timestep = timestep

        self.root = pg.init()
        self.canvas = pg.display.set_mode((width, height))
        self.running = False
        self.timer = pg.time.Clock()
        self.objects: list[SimulationObject] = []

        pg.display.set_caption(title)

    def _run(self):
        while self.running:
            self.update_velocity()
            self.update()
            self.canvas.fill((0,0,0))
            self.paint()
            self.timer.tick(self.timestep)
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()


    def add_object(self, object: SimulationObject):
        self.objects.append(object)

    def remove_object(self, object: SimulationObject):
        self.objects.remove(object)

    def get_objects(self):
        return self.objects

    def get_engine_clock(self):
        return self.timer.get_time()

    def get_engine_framerate(self):
        return self.timestep

    def update_velocity(self):
        for obj in self.objects:
            obj.update_velocity(self.objects)

    def update(self):
        for obj in self.objects:
            obj.update()

    def paint(self):
        for obj in self.objects:
            obj.paint(self.canvas)

    def run(self):
        self.running = True
        self._run()

    def quit(self):
        self.running = False
        pg.quit()
        sys.exit()
