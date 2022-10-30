import tkinter as Tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from robot_arm import RobotArm
from utils.get_joint_coords import get_joint_coords


class Model:
    def __init__(self):
        self.robot = None
        self.goal_pos = None
        self.res = None

    def calculate_joint_coords(self):
        x_coords = get_joint_coords(self.robot)
        y_coords = self.y_point
        self.res = {"x": x_coords, "y": y_coords}


class View:
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        self.fig = Figure(figsize=(7.5, 4), dpi=80)
        self.ax0 = self.fig.add_axes(
            (0.05, .05, .90, .90), facecolor=(.75, .75, .75), frameon=False)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.sidepanel = SidePanel(master)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas.draw()


class SidePanel:
    def __init__(self, root):
        self.frame2 = Tk.Frame(root)
        self.frame2.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.x_val_label = Tk.Label(self.frame2, text="X Value")
        self.x_val_label.pack(side="top", fill=Tk.BOTH)
        self.x_val_entry = Tk.Entry(self.frame2)
        self.x_val_entry.pack(side="top", fill=Tk.BOTH)
        self.y_val_label = Tk.Label(self.frame2, text="Y Value")
        self.y_val_label.pack(side="top", fill=Tk.BOTH)
        self.y_val_entry = Tk.Entry(self.frame2)
        self.y_val_entry.pack(side="top", fill=Tk.BOTH)
        self.plotBut = Tk.Button(self.frame2, text="Plot")
        self.plotBut.pack(side="top", fill=Tk.BOTH)
        self.clearButton = Tk.Button(self.frame2, text="Clear")
        self.clearButton.pack(side="top", fill=Tk.BOTH)


class Controller:
    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root)
        self.view.sidepanel.plotBut.bind("<Button>", self.my_plot)
        self.view.sidepanel.clearButton.bind("<Button>", self.clear)

    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        self.root.mainloop()

    def clear(self, event):
        self.view.ax0.clear()
        self.view.fig.canvas.draw()

    def my_plot(self, event):
        self.model.robot = RobotArm(lengths=[1, 1], origin=(0, 0))
        self.model.goal_pos = (self.view.sidepanel.x_val_entry, self.view.sidepanel.y_val_entry)
        self.model.calculate_joint_coords()
        self.view.ax0.clear()
        self.view.ax0.scatter(
            self.model.res["x"], self.model.res["y"])
        self.view.fig.canvas.draw()


if __name__ == '__main__':
    c = Controller()
    c.run()
