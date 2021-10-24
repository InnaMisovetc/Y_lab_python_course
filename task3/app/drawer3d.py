import math

import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from task3.app.calculator_3d import SquarePyramid, RightCircularCone, Cylinder, Sphere, Cuboid, Cube


class Drawer3D:
    POINTS_COUNT = 20

    @staticmethod
    def draw_pyramid(figure, pyramid: SquarePyramid) -> None:
        x = pyramid.x
        height = pyramid.height
        ax = figure.add_subplot(111, projection='3d')
        v = np.array([[0, 0, 0], [x, 0, 0], [x, x, 0], [0, x, 0], [x / 2, x / 2, height]])

        polygons = [[v[0], v[1], v[4]], [v[0], v[3], v[4]], [v[2], v[1], v[4]], [v[2], v[3], v[4]],
                    [v[0], v[1], v[2], v[3]]]

        ax.add_collection3d(Poly3DCollection(polygons, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
        ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

        Drawer3D.set_labels(ax)

    @staticmethod
    def draw_cone(figure, cone: RightCircularCone):
        ax = figure.add_subplot(111, projection='3d')
        v = [[0, 0, cone.height]]
        v.extend(Drawer3D.get_circle_points(cone.radius))
        v = np.array(v)

        polygons = []
        for i in range(1, Drawer3D.POINTS_COUNT):
            polygons.append([v[0], v[i], v[i + 1]])  # Adding sides
        polygons.append([v[0], v[1], v[len(v) - 1]])  # Adding last side
        polygons.append(v[1:])  # Adding bottom

        ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
        ax.add_collection3d(Poly3DCollection(polygons, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

        Drawer3D.set_labels(ax)

    @staticmethod
    def draw_cylinder(figure, cylinder: Cylinder):
        ax = figure.add_subplot(111, projection='3d')

        v = Drawer3D.get_circle_points(cylinder.radius, 0)
        v.extend(Drawer3D.get_circle_points(cylinder.radius, cylinder.height))
        v = np.array(v)

        polygons = []
        for i in range(Drawer3D.POINTS_COUNT - 1):
            polygons.append([v[i], v[i + 1], v[Drawer3D.POINTS_COUNT + 1 + i], v[Drawer3D.POINTS_COUNT + i]])

        polygons.append(
            [v[0], v[Drawer3D.POINTS_COUNT - 1], v[Drawer3D.POINTS_COUNT * 2 - 1], v[Drawer3D.POINTS_COUNT]])
        polygons.append(v[:Drawer3D.POINTS_COUNT])
        polygons.append(v[Drawer3D.POINTS_COUNT:])

        ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
        ax.add_collection3d(Poly3DCollection(polygons, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

        Drawer3D.set_labels(ax)

    @staticmethod
    def draw_sphere(figure, sphere: Sphere):
        ax = figure.add_subplot(111, projection='3d')
        u, v = np.mgrid[0:2 * np.pi:Drawer3D.POINTS_COUNT * 1j, 0:np.pi:Drawer3D.POINTS_COUNT * 1j]

        x = np.cos(u) * np.sin(v) * sphere.radius
        y = np.sin(u) * np.sin(v) * sphere.radius
        z = np.cos(v) * sphere.radius

        ax.scatter3D(x, y, z)
        ax.plot_surface(x, y, z, color='cyan', alpha=0.25)
        ax.plot_wireframe(x, y, z, color='r', linewidth=1)

        Drawer3D.set_labels(ax)

    @staticmethod
    def draw_cuboid(figure, cuboid: Cuboid):
        ax = figure.add_subplot(111, projection='3d')

        v = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]]
        v = np.array([[x[0] * cuboid.a, x[1] * cuboid.b, x[2] * cuboid.h] for x in v])

        polygons = [[v[0], v[1], v[2], v[3]], [v[4], v[5], v[6], v[7]],
                    [v[0], v[1], v[5], v[4]], [v[1], v[2], v[6], v[5]],
                    [v[2], v[3], v[7], v[6]], [v[3], v[0], v[4], v[7]]]

        ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
        ax.add_collection3d(Poly3DCollection(polygons, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

        Drawer3D.set_labels(ax)

    @staticmethod
    def draw_cube(figure, cube: Cube):
        Drawer3D.draw_cuboid(figure, cube)

    @staticmethod
    def get_circle_points(radius, z=0.0, points_count=POINTS_COUNT):
        v = []
        for i in range(0, points_count):
            angle = (2 * math.pi / points_count) * i
            x, y = math.cos(angle) * radius, math.sin(angle) * radius
            v.append([x, y, z])
        return v

    @staticmethod
    def set_labels(ax):
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        Drawer3D.set_axes_equal(ax)

    @staticmethod
    def set_axes_equal(ax):
        """Make axes of 3D plot have equal scale so that spheres appear as spheres,
        cubes as cubes, etc..  This is one possible solution to Matplotlib's
        ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

        Input
          ax: a matplotlib axis, e.g., as output from plt.gca().
        """

        x_limits = ax.get_xlim3d()
        y_limits = ax.get_ylim3d()
        z_limits = ax.get_zlim3d()

        x_range = abs(x_limits[1] - x_limits[0])
        x_middle = np.mean(x_limits)
        y_range = abs(y_limits[1] - y_limits[0])
        y_middle = np.mean(y_limits)
        z_range = abs(z_limits[1] - z_limits[0])
        z_middle = np.mean(z_limits)

        # The plot bounding box is a sphere in the sense of the infinity
        # norm, hence I call half the max range the plot radius.
        plot_radius = 0.5*max([x_range, y_range, z_range])

        ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
        ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
        ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])
