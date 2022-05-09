from tkinter import *

app = Tk()
canvas = Canvas(app, width=900, height=600)
canvas.pack()

# T
# xi, yi, xf, yf
canvas.create_rectangle(250, 30, 450, 80, outline='#005397', fill='#005397')
canvas.create_rectangle(325, 80, 375, 340, outline='#005397', fill='#005397')

# U
canvas.create_rectangle(50, 130, 275, 180, outline='#005397', fill='#005397')
canvas.create_rectangle(225, 180, 275, 410, outline='#005397', fill='#005397')
canvas.create_rectangle(225, 360, 425, 410, outline='#005397', fill='#005397')
canvas.create_rectangle(425, 410, 475, 180, outline='#005397', fill='#005397')
canvas.create_rectangle(425, 130, 850, 180, outline='#005397', fill='#005397')

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

