import inspect
import tkinter as tk
from collections.abc import Iterable

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


from task3.app.calculator import ResultPrinter
from task3.app.calculator_2d import Circle, Rectangle, Square, Trapezoid, Diamond, Triangle
from task3.app.calculator_3d import Sphere, Cuboid, Cube, Cylinder, RightCircularCone, SquarePyramid
from task3.app.drawer2d import Drawer2D
from task3.app.drawer3d import Drawer3D


class WelcomeWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.shapes_2d = {'circle': ShapeWindow(self, Circle(1), Drawer2D.draw_circle).show,
                          'rectangle': ShapeWindow(self, Rectangle(1, 2), Drawer2D.draw_rect).show,
                          'square': ShapeWindow(self, Square(1), Drawer2D.draw_quad).show,
                          'trapezoid': ShapeWindow(self, Trapezoid(4, 90, 45, 1), Drawer2D.draw_trapezoid).show,
                          'diamond': ShapeWindow(self, Diamond(1, 2), Drawer2D.draw_diamond).show,
                          'triangle': ShapeWindow(self, Triangle(2, 3, 3), Drawer2D.draw_triangle).show}
        self.shapes_3d = {'sphere': ShapeWindow(self, Sphere(1), Drawer3D.draw_sphere).show,
                          'parallelepiped': ShapeWindow(self, Cuboid(1, 2, 3), Drawer3D.draw_cuboid).show,
                          'cube': ShapeWindow(self, Cube(1), Drawer3D.draw_cube).show,
                          'cylinder': ShapeWindow(self, Cylinder(1, 3), Drawer3D.draw_cylinder).show,
                          'cone': ShapeWindow(self, RightCircularCone(1, 3), Drawer3D.draw_cone).show,
                          'pyramid': ShapeWindow(self, SquarePyramid(1, 3), Drawer3D.draw_pyramid).show}

    def main_window(self):
        self.window.title('Graphical Calculator')
        self.window.resizable(False, False)
        self.create_labels()
        self.create_buttons()
        self.window.mainloop()

    def create_labels(self):
        label_2d = tk.Label(self.window, text='2D shapes')
        label_3d = tk.Label(self.window, text='3D shapes')
        label_2d.grid(row=0, column=0)
        label_3d.grid(row=0, column=1)

    def create_buttons(self):
        row = 1
        for shape_2d, shape_3d in zip(self.shapes_2d, self.shapes_3d):
            my_button_x = tk.Button(self.window, text=shape_2d, width=10, command=self.shapes_2d[shape_2d])
            my_button_x.grid(row=row, column=0)
            my_button_y = tk.Button(self.window, text=shape_3d, width=10, command=self.shapes_3d[shape_3d])
            my_button_y.grid(row=row, column=1)
            row += 1


class ShapeWindow:
    def __init__(self, main_window, shape, draw_method=None):
        self.main_window = main_window
        self.shape = shape
        self.draw_method = draw_method
        self.window = None
        self.fields_entries = {}

    def draw_entry(self, header, row, value):
        header = header.capitalize()
        label = tk.Label(self.window, text=f'{header}:')
        label.grid(row=row, column=0)
        entry = tk.Entry(self.window)
        entry.grid(row=row, column=1)
        entry.insert(0, ResultPrinter.round_result(value))
        return entry

    def draw_label(self, method, row, value):
        method = method.replace('get_', '')
        method = method.capitalize()
        if isinstance(value, Iterable):
            value = [str(ResultPrinter.round_result(v)) for v in value]
            value = ', '.join(value)
        else:
            value = ResultPrinter.round_result(value)
        label = tk.Label(self.window, text=f'{method}:')
        label.grid(row=row, column=0)
        label = tk.Label(self.window, text=f'{value}')
        label.grid(row=row, column=1)
        return label

    def show(self):
        self.window = tk.Toplevel(self.main_window.window)
        self.window.resizable(False, False)
        self.window.title('Enter shape parameters')

        fig = Figure(figsize=plt.figaspect(1), dpi=100)
        self.draw_method(fig, self.shape)
        canvas = FigureCanvasTkAgg(fig, master=self.window)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(columnspan=2)

        row = 1
        shape_fields = inspect.signature(type(self.shape).__init__)
        shape_args = list(shape_fields.parameters.values())[1:]
        for arg in shape_args:
            value = getattr(self.shape, arg.name)
            entry = self.draw_entry(arg.name, row, value)
            self.fields_entries[arg.name] = entry
            row += 1

        shape_methods = [method for method in dir(self.shape) if method.startswith('get_')]
        for method in shape_methods:
            value = getattr(type(self.shape), method)(self.shape)
            self.draw_label(method, row, value)
            row += 1

        refresh_button = tk.Button(self.window, text='Refresh', command=self.refresh)
        refresh_button.grid(row=row + 1, column=0, columnspan=2)

    def refresh(self):
        args = []
        for field in self.fields_entries:
            new_value = float(self.fields_entries[field].get())
            args.append(new_value)
        new_shape = (type(self.shape))(*args)
        ShapeWindow(self.main_window, new_shape, self.draw_method).show()
        self.window.destroy()
