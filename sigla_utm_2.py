from tkinter import *
from math import sqrt

app = Tk()
canvas = Canvas(app, width=900, height=600)
canvas.pack()

def create_circle_arc(canvas, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return canvas.create_arc(x-r, y-r, x+r, y+r, **kwargs)


# Lines
canvas.create_line(100, 255, 875, 255, fill='#005397', width = 3)
canvas.create_line(100, 285, 875, 285, fill='#005397', width = 3)
canvas.create_line(100, 315, 875, 315, fill='#005397', width = 3)


# T
canvas.create_rectangle(250, 30, 450, 80, outline='#005397', fill='#005397')
canvas.create_rectangle(325, 80, 375, 340, outline='#005397', fill='#005397')


# U
canvas.create_polygon([175, 180,
                       125, 180 + 24,
                       82, 180 + 24 - 30,
                       150, 136], outline='#005397', fill='#005397')
create_circle_arc(canvas, 175, 180, 50, outline='#005397', fill='#005397', start = 90, end=120)

canvas.create_rectangle(175, 130, 225, 180, outline='#005397', fill='#005397')
create_circle_arc(canvas, 225, 180, 50, outline='#005397', fill='#005397')

create_circle_arc(canvas, 200, 205, 50, outline='#005397', fill='#005397', start = 90, end=0)
create_circle_arc(canvas, 200, 205, 24, outline='#F0F0F0', fill='#F0F0F0', start = 90, end=0)

canvas.create_rectangle(225, 180, 275, 360, outline='#005397', fill='#005397')
create_circle_arc(canvas, 275, 360, 50, outline='#005397', fill='#005397', start=180, end=270)

create_circle_arc(canvas, 300, 335, 50, outline='#005397', fill='#005397', start=180, end=270)
create_circle_arc(canvas, 300, 335, 24, outline='#F0F0F0', fill='#F0F0F0', start=180, end=270)

canvas.create_rectangle(275, 360, 425, 410, outline='#005397', fill='#005397')
create_circle_arc(canvas, 425, 360, 50, outline='#005397', fill='#005397', start=0, end=-90)

create_circle_arc(canvas, 400, 335, 50, outline='#005397', fill='#005397', start=0, end=-90)
create_circle_arc(canvas, 400, 335, 24, outline='#F0F0F0', fill='#F0F0F0', start=0, end=-90)

canvas.create_rectangle(425, 360, 475, 180, outline='#005397', fill='#005397')
create_circle_arc(canvas, 475, 180, 50, outline='#005397', fill='#005397', start=90, end=180)

create_circle_arc(canvas, 500, 205, 50, outline='#005397', fill='#005397', start=90, end=180)
create_circle_arc(canvas, 500, 205, 24, outline='#F0F0F0', fill='#F0F0F0', start=90, end=180)

canvas.create_rectangle(475, 130, 850, 180, outline='#005397', fill='#005397')

# M
canvas.create_rectangle(500, 30, 550, 340, outline='#005397', fill='#005397')
canvas.create_polygon([500, 30,
                       550, 30,
                       650, 340,
                       600, 340], outline='#005397', fill='#005397')

canvas.create_polygon([650, 340,
                       600, 340,
                       700, 30,
                       750, 30], outline='#005397', fill='#005397')

canvas.create_rectangle(700, 30, 750, 340, outline='#005397', fill='#005397')



if __name__ == '__main__':
    mainloop()

