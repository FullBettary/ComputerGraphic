import tkinter as tk
import Moduls


class Entry:
    def __init__(self, root, t1=0, t2=0, t3=0):
        self.e = [tk.Entry(root, width=5) for i in range(3)]

        self.e[0].insert(tk.END, t1)
        self.e[1].insert(tk.END, t2)
        self.e[2].insert(tk.END, t3)

        c = ['x', 'y', 'z']
        for i in range(3):
            tk.Label(root, text=c[i]).pack(side=tk.LEFT)
            self.e[i].pack(side=tk.LEFT, padx=5, pady=5)

    def get_value(self):
        l = []
        for i in range(3):
            l.append(int(self.e[i].get()))
        return l

def InputMenu():

    points = []

    def check_status(a, b, c):
        status = Moduls.exist_triangle(a, b, c)
        if not status:
            tk.Label(frame3, text='Треугольник не корректен!').pack(side=tk.BOTTOM)
        else:
            tk.Label(frame3, text='Треугольник сохранен').pack(side=tk.BOTTOM)
            points.append([a, b, c])


    root = tk.Tk()

    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    frame3 = tk.Frame(root)
    frame_line1 = tk.Frame(frame2)
    frame_line2 = tk.Frame(frame2)
    frame_line3 = tk.Frame(frame2)

    frame1.pack()
    frame2.pack()
    frame3.pack()
    frame_line1.pack()
    frame_line2.pack()
    frame_line3.pack()

    tk.Label(frame1, text='Введите координаты точек треугольника').pack()

    e11 = Entry(frame_line1, 20, 90, 10)
    e12 = Entry(frame_line2, 135, 40, 100)
    e13 = Entry(frame_line3, 60, 10, 95)

    b = tk.Button(frame3, text='Проверить корректность треугольника',
                  command=lambda: check_status(e11.get_value(), e12.get_value(), e13.get_value()))
    b.pack(side=tk.TOP)

    root.mainloop()

    return points
