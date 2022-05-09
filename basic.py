import tkinter.font
from tkinter import *
import math

class Flag:
    def __init__(self, canvas, n_section=3, horizontal=False, colors =['blue', 'yellow', 'red'], country_name='Xd'):
        self.canvas = canvas
        self.n_section = n_section
        self.horizontal = horizontal
        self.colors = colors
        self.country_name = country_name
        if self.n_section != len(self.colors): self.n_section = len(self.colors)

        self.canvas.create_rectangle(0,0,20,500, fill='brown')
        self.horizontal_sections() if horizontal else self.vertical_sections()
        self.virtual_signature()


    def horizontal_sections(self):
        for index in range(self.n_section):
            self.canvas.create_rectangle(20, int(index*int(250/self.n_section)),
                                        500, int((index+1)*int(250/self.n_section)),
                                        fill=self.colors[index], outline=self.colors[index])


    def vertical_sections(self):
        for index in range(self.n_section):
            self.canvas.create_rectangle(int(index * int(480 / self.n_section))+20, 0,
                                        int((index + 1) * int(480 / self.n_section))+20, 250,
                                        fill=self.colors[index], outline=self.colors[index])

    def virtual_signature(self, student='Perebinos Daniel'):
        self.canvas.create_text(80,350, text=f'Drapel {self.country_name}', font=tkinter.font.Font(family='Helvetica',
        size=16), fill='blue', anchor=tkinter.W)
        self.canvas.create_text(80, 380, text=f'Student {student}', font=tkinter.font.Font(family='Helvetica',
                                size=16), fill='gold', anchor=tkinter.W)
        self.canvas.create_text(80, 410, text='UTM, FCIM, Gr. IA-203', font=tkinter.font.Font(family='Helvetica',
                                size=16), fill='red', anchor=tkinter.W)


class Circle:
    def __init__(self, canvas, x=2, y=2, r=1, color = 'red', outline='black'):
        self.x = x
        self.y = y
        self.r = r
        self.canvas = canvas
        self.color = color
        self.outline = outline

        self.__create_circle()

    def __create_circle(self):
        x0 = self.x - self.r
        y0 = self.y - self.r
        x1 = self.x + self.r
        y1 = self.y + self.r
        return self.canvas.create_oval(x0, y0, x1, y1, fill=self.color, outline=self.outline)


class Star:
    def __init__(self, canvas, x=150, y=150, r=20, color='yellow', n = 5, right=True, rotation = 0):
        self.x = x
        self.y = y
        self.r = r
        self.n = n
        self.right = right
        self.canvas = canvas
        self.color = color
        self.rotation = rotation


        self.__create()

    def __create(self):
        # Place the five points of the five-pointed star in turn

        if self.n != 5 or not self.right:
            points = []
            for i in range(self.n):
                points.append(self.x + int(self.r * math.sin(i * 2 * math.pi / self.n + self.rotation)))
                points.append(self.y + int(self.r * math.cos(i * 2 * math.pi / self.n + self.rotation)))

                points.append(self.x + int(0.5*self.r * math.sin(i * 2 * math.pi / self.n + math.pi / self.n + self.rotation)))
                points.append(self.y + int(0.5*self.r * math.cos(i * 2 * math.pi / self.n + math.pi / self.n + self.rotation)))
        else:
            points = [
                #
                self.x - int(self.r * math.sin(2 * math.pi / 5)),
                self.y - int(self.r * math.cos(2 * math.pi / 5)),

                #
                self.x + int(self.r * math.sin(2 * math.pi / 5)),
                self.y - int(self.r * math.cos(2 * math.pi / 5)),

                #
                self.x - int(self.r * math.sin(math.pi / 5)),
                self.y + int(self.r * math.cos(math.pi / 5)),

                # vertex
                self.x,
                self.y - self.r,

                #
                self.x + int(self.r * math.sin(math.pi / 5)),
                self.y + int(self.r * math.cos(math.pi / 5))
        ]
        # Create a polygon based on ten vertices
        self.canvas.create_polygon(points, fill=self.color)







if __name__ == '__main__':
    root = Tk()
    root.title('Drapel Test')
    root.geometry('500x500')

    canvas = Canvas(root, width=500, height = 500, bg='white')
    canvas.pack()

    f = Flag(canvas, horizontal=True)
    # s = Star(canvas, 260, 125, 30, color='black')


    root.mainloop()