import math

import numpy as np
from matplotlib import pyplot as plt

from task3.app.calculator_2d import Circle, Rectangle, Square, Triangle, Trapezoid, Diamond


class Drawer2D:

    @staticmethod
    def draw_circle(figure, circle: Circle):
        ax = Drawer2D.add_subplot(figure)
        theta = np.linspace(0, 2 * np.pi, 100)
        ax.plot(circle.radius * np.cos(theta), circle.radius * np.sin(theta), color='r')
        circle = plt.Circle((0, 0), circle.radius, facecolor='cyan', linewidth=1, alpha=.25)
        ax.add_artist(circle)

    @staticmethod
    def draw_rect(figure, rect: Rectangle):
        ax = Drawer2D.add_subplot(figure)
        v = np.array([[0, 0], [rect.x, 0], [rect.x, rect.y], [0, rect.y], [0, 0]])
        ax.plot(v[:, 0], v[:, 1], '-o')
        rect = plt.Rectangle([0, 0], rect.x, rect.y, facecolor='cyan', linewidth=1, alpha=.25)
        ax.add_artist(rect)

    @staticmethod
    def draw_quad(figure, quad: Square):
        Drawer2D.draw_rect(figure, quad)

    @staticmethod
    def draw_triangle(figure, triangle: Triangle):
        ax = Drawer2D.add_subplot(figure)
        alpha = math.asin((triangle.x ** 2 + triangle.y ** 2 - triangle.z ** 2) / (2 * triangle.x * triangle.y))
        x, y = triangle.y * math.sin(alpha), triangle.y * math.cos(alpha)
        v = np.array([[0, 0], [triangle.x, 0], [x, y], [0, 0]])
        ax.plot(v[:, 0], v[:, 1], '-o')
        triangle = plt.Polygon(v, facecolor='cyan', linewidth=1, alpha=.25)
        ax.add_artist(triangle)

    @staticmethod
    def draw_trapezoid(figure, trapezoid: Trapezoid):
        ax = Drawer2D.add_subplot(figure)
        a1 = math.radians(trapezoid.left_base_angle)
        a2 = math.radians(trapezoid.right_base_angle)
        x1 = trapezoid.height / math.sin(a1) * math.cos(a1)
        x2 = trapezoid.height / math.sin(a2) * math.cos(a2)
        v = np.array([[0, 0], [trapezoid.base, 0], [trapezoid.base - x2, trapezoid.height], [x1, trapezoid.height], [0, 0]])
        ax.plot(v[:, 0], v[:, 1], '-o')
        trapezoid = plt.Polygon(v, facecolor='cyan', linewidth=1, alpha=.25)
        ax.add_artist(trapezoid)

    @staticmethod
    def draw_diamond(figure, diamond: Diamond):
        ax = Drawer2D.add_subplot(figure)
        v = np.array([[0, -diamond.d2/2], [diamond.d1/2, 0], [0, diamond.d2/2], [-diamond.d1/2, 0], [0, -diamond.d2/2]])
        ax.plot(v[:, 0], v[:, 1], '-o')
        diamond = plt.Polygon(v, facecolor='cyan', linewidth=1, alpha=.25)
        ax.add_artist(diamond)

    @staticmethod
    def add_subplot(figure):
        ax = figure.add_subplot(111)
        ax.set_aspect('equal')
        return ax
