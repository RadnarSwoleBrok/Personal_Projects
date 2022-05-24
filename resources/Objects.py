from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from Gravity_Simulator.Engine.Display.PyGameEngine import SimulationObject
import pygame as pg

@dataclass(slots=True)
class Planet(SimulationObject):
    """
    Simulation Object representing a planetary body for a star system simulation.
    How the object should be rendered is implemented here. Allows interfacing with
    planetary simulation.

    position: Optional[np.array([float])]
    velocity: Optional[np.array([float])]
    mass: float
    radius: float
    color: tuple[int]
    scale: int
    """
    position: np.array([float])
    velocity: np.array([float])
    mass: float
    radius: float
    color: tuple[int, ...]
    scale: int
    orbital_path = np.array([np.array([float])])
    timestep: int = 3600 # one day in seconds
    isSun: bool = False

    def compute_GForce_vectors(self, other, g_constant=6.67428e-11):
        sqr_distance = np.linalg.norm(other.position - self.position) ** 2
        if sqr_distance == 0:
            sqr_distance += 0.1
        scaled_distance = sqr_distance * 1.496e+8 #astronomical unit in KM
        mass_area = self.mass * other.mass
        force = g_constant * np.divide(mass_area, scaled_distance)
        theta = np.arctan2((other.position[1] - self.position[1]), (other.position[0] - self.position[0]))
        x_force = np.cos(theta) * force
        y_force = np.sin(theta) * force
        return x_force, y_force

    def compute_forces(self, other):
        return self.compute_GForce_vectors(other)

    def update_velocity(self, objects: list[Planet]):
        total_fx = total_fy = 0
        for body in objects:
            if body.isSun and self.isSun:
                continue
            fx, fy = self.compute_forces(body)
            total_fx += fx
            total_fy += fy
        updated_velocity = np.array([total_fx / self.mass * self.timestep, total_fy / self.mass * self.timestep])
        self.velocity = np.add(self.velocity, updated_velocity)

    def update(self):
        self.position = np.add(self.position, self.velocity)
        np.append(self.orbital_path, self.position)

    def paint(self, canvas: pg.display):
        updated_points = []
        if len(self.orbital_path) > 1:
            for point in self.orbital_path:
                x, y = point[0], point[1]
                x = x * self.scale + canvas.get_width() / 2
                y = y * self.scale + canvas.get_height() / 2
                updated_points.append((x, y))
                pg.draw.lines(canvas, (255, 255, 255), False, updated_points, 2)
        pg.draw.circle(canvas, self.color, (self.position[0] + canvas.get_width() / 2,
                                            self.position[1] + canvas.get_height() / 2),
                                            self.radius)




