import math
from tkinter import *
from basic import Flag, Circle, Star

# Intro
root = Tk()
root.title('Drapele')
root.geometry('500x500')

canvas = Canvas(root, width=500, height = 500, bg='white')
canvas.pack()



# Flags
# Usoare

# Armenia
f = Flag(canvas, horizontal=True, colors=['red', 'blue', 'orange'], country_name='Armenia')

# Austria
# f = Flag(canvas, horizontal=True, colors=['red', 'white', 'red'], country_name='Austria')

# Bangladesh
# f = Flag(canvas, horizontal=True, colors=['green'], country_name='Bangladesh')
# c = Circle(canvas, 260, 125, 100)

# Belgia
# f = Flag(canvas, colors=['black', 'yellow', 'red'], country_name='Belgia')

# Benin
# f = Flag(canvas, horizontal=True, colors=['yellow', 'red'], country_name='Benin')
# canvas.create_rectangle(20,0,200, 250, fill='green')

# Bulgaria
# f = Flag(canvas, horizontal=True, colors=['white','green', 'red'], country_name='Bulgaria')

# Cehia
# f = Flag(canvas, horizontal=True, colors=['white','red'], country_name='Cehia')
# canvas.create_polygon([20,0,
#                        200,125,
#                        20, 250], fill='blue')

# Ciad
# f = Flag(canvas, country_name='Ciad')

# Columbia
# f = Flag(canvas, horizontal=True, colors=['yellow','red'], country_name='Columbia')
# canvas.create_rectangle(20,125,500,185, fill='blue')

# Rep. Congo (Brazaville)
# f = Flag(canvas, horizontal=True, colors=['yellow'], country_name='Rep. Congo (Brazaville)')
# canvas.create_polygon([20,0, 320,0, 20,250], fill='green')
# canvas.create_polygon([180,250, 500,0, 500,250], fill='red')

# Costa Rica
# f = Flag(canvas, horizontal=True, colors=['white', 'red', 'white'], country_name='Costa Rica')
# canvas.create_rectangle(20,0,500, 40, fill='blue')
# canvas.create_rectangle(20,210,500,250, fill='blue')

# Estonia
# f = Flag(canvas, horizontal=True, colors=['cyan', 'black', 'white'], country_name='Estonia')

# Franta
# f = Flag(canvas, horizontal=False, colors=['blue', 'white', 'red'], country_name='Franta')

# Gabon
# f = Flag(canvas, horizontal=True, colors=['green', 'yellow', 'cyan'], country_name='Gabon')

# Germania
# f = Flag(canvas, horizontal=True, colors=['black', 'red', 'yellow'], country_name='Germania')

# Guineea
# f = Flag(canvas, horizontal=False, colors=['red', 'yellow', 'green'], country_name='Guineea')

# Indonezia
# f = Flag(canvas, horizontal=True, colors=['red', 'white'], country_name='Indonezia')

# Irlanda
# f = Flag(canvas, horizontal=False, colors=['green', 'white', 'orange'], country_name='Irlanda')

# Italia
# f = Flag(canvas, horizontal=False, colors=['green', 'white', 'red'], country_name='Italia')

# Japonia
# f = Flag(canvas, horizontal=False, colors=['white'], country_name='Japonia')
# c = Circle(canvas, 260, 125, 100)

# Letonia
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Letonia')
# canvas.create_rectangle(20, 100 , 500, 150, fill='white')

# Lituania
# f = Flag(canvas, horizontal=True, colors=['yellow', 'green', 'red'], country_name='Lituania')

# Luxemburg
# f = Flag(canvas, horizontal=True, colors=['red', 'white', 'cyan'], country_name='Luxemburg')

# Madagascar
# f = Flag(canvas, horizontal=True, colors=['red', 'green'], country_name='Madagascar')
# canvas.create_rectangle(20, 0, 200, 250, fill='white')

# Mali
# f = Flag(canvas, horizontal=False, colors=['green', 'yellow', 'red'], country_name='Mali')

# Mauritius
# f = Flag(canvas, horizontal=True, colors=['red', 'blue', 'yellow', 'green'], country_name='Mauritius')

# Moldova
# f = Flag(canvas, country_name='Moldova')

# Monaco
# f = Flag(canvas, horizontal=True, colors=['red', 'white'], country_name='Monaco')

# Nigeria
# f = Flag(canvas, horizontal=False, colors=['green', 'white', 'green'], country_name='Nigeria')

# Olanda
# f = Flag(canvas, horizontal=True, colors=['red', 'white', 'blue'], country_name='Olanda')

# Palau
# f = Flag(canvas, horizontal=False, colors=['cyan'], country_name='Palau')
# c = Circle(canvas, 260, 125, 100, color='yellow')

# Polonia
# f = Flag(canvas, horizontal=True, colors=['white', 'red'], country_name='Polonia')

# Romania
# f = Flag(canvas, country_name='Romania')

# Rusia
# f = Flag(canvas, horizontal=True, colors=['white', 'blue', 'red'], country_name='Rusia')

# Sierra Leone
# f = Flag(canvas, horizontal=True, colors=['green', 'white', 'cyan'], country_name='Sierra Leone')

# Tailanda
# f = Flag(canvas, horizontal=True, colors=['white', 'purple', 'white'], country_name='Tailanda')
# canvas.create_rectangle(20, 0, 500, 40, fill='red')
# canvas.create_rectangle(20, 250, 500, 210, fill='red')

# Ungaria
# f = Flag(canvas, horizontal=True, colors=['red', 'white', 'olive drab'], country_name='Ungaria')

# Ucraina
# f = Flag(canvas, horizontal=True, colors=['blue', 'yellow'], country_name='Ucraina')

# Yemen
# f = Flag(canvas, horizontal=True, colors=['red', 'white', 'black'], country_name='Yemen')








# Mediu

# Bahamas
# f = Flag(canvas, horizontal=True, colors=['cyan', 'yellow', 'cyan'], country_name='Bahamas')
# canvas.create_polygon(20,0, 230,125, 20,250)

# Bahrain
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Bahrain')
# canvas.create_polygon(20,0, 180,0,
#
#                       220,20, 180,40, 220,60, 180,80, 220,100,
#                       180,120, 220,140, 180,160, 220,180,
#                       180,200, 220,220, 180,240, 220,260,
#
#                       180,250, 20,250,
#                       fill='white')

# Borswana
# f = Flag(canvas, horizontal=True, colors=['royal blue'], country_name='Borswana')
# canvas.create_rectangle(20, 100, 500, 150, fill='white')
# canvas.create_rectangle(20, 110, 500, 140, fill='black')

# Burkina Faso
# f = Flag(canvas, horizontal=True, colors=['red', 'green'], country_name='Burkina Faso')
# s = Star(canvas, 260, 125, 40)

# Camerun
# f = Flag(canvas, horizontal=False, colors=['green', 'red', 'yellow'], country_name='Camerun')
# s = Star(canvas, 260, 125, 40)

# Rep. Centrafricana
# f = Flag(canvas, horizontal=True, colors=['blue', 'white', 'green', 'yellow'], country_name='Rep. Centrafricana')
# s = Star(canvas, 50, 31, 20)
# canvas.create_rectangle(230, 0, 290, 250, fill='red')

# Chile
# f = Flag(canvas, horizontal=True, colors=['white', 'red'], country_name='Chile')
# canvas.create_rectangle(20, 0, 180, 125, fill='blue')
# s = Star(canvas, 100, 60, 40, color='white')

# Danemarca
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Danemarca')
# canvas.create_rectangle(20,100, 500,150, fill='white')
# canvas.create_rectangle(160,0, 210,250, fill='white')

# Elvetia
# f = Flag(canvas, horizontal=False, colors=['red', 'white'], country_name='Elvetia')
# canvas.create_rectangle(120,50, 160,200, fill='white')
# canvas.create_rectangle(65,105, 215,145, fill='white')

# Emiratele Arabe Unite
# f = Flag(canvas, horizontal=True, colors=['green', 'white', 'black'], country_name='Emiratele Arabe Unite')
# canvas.create_rectangle(20, 0, 140, 250, fill='red')

# Finlanda
# f = Flag(canvas, horizontal=True, colors=['white'], country_name='Finlanda')
# canvas.create_rectangle(20,100, 500,150, fill='blue')
# canvas.create_rectangle(160,0, 210,250, fill='blue')

# Gambia
# f = Flag(canvas, horizontal=True, colors=['red', 'white', 'green'], country_name='Gambia')
# canvas.create_rectangle(20, 100, 500, 150, fill='blue')

# Ghana
# f = Flag(canvas, horizontal=True, colors=['red', 'yellow', 'green'], country_name='Ghana')
# s = Star(canvas, 260, 125, 40, color='black')

# Islanda
# f = Flag(canvas, horizontal=True, colors=['blue'], country_name='Islanda')
# canvas.create_rectangle(20,100, 500,150, fill='white')
# canvas.create_rectangle(160,0, 210,250, fill='white')
# canvas.create_rectangle(20,110, 500,140, fill='red')
# canvas.create_rectangle(170,0, 200,250, fill='red')

# Jamaica
# f = Flag(canvas, horizontal=True, colors=['green'], country_name='Jamaica')
# canvas.create_polygon(20,0, 40,0, 280,125, 40,250, 20,250, fill='yellow')
# canvas.create_polygon(500,0, 480,0, 240,125, 480,250, 500,250, fill='yellow')
# canvas.create_polygon(20,20, 220,125, 20,230, fill='black')
# canvas.create_polygon(500,20, 300,125, 500,230, fill='black')

# Kuwait
# f = Flag(canvas, horizontal=True, colors=['green', 'white', 'red'], country_name='Kuwait')
# canvas.create_polygon(20,0, 120,83, 120,166, 20,250)

# Laos
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Laos')
# canvas.create_rectangle(20, 50, 500, 200, fill='blue')
# c = Circle(canvas, 260, 125, 70, color='white')

# Myanmar
# f = Flag(canvas, horizontal=True, colors=['yellow', 'green', 'red'], country_name='Myanmar')
# s = Star(canvas, 260, 125, 90, color='white')

# Niger
# f = Flag(canvas, horizontal=True, colors=['orange', 'white', 'green'], country_name='Niger')
# c = Circle(canvas, 260, 125, 30, color='orange')

# Norvegia
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Norvegia')
# canvas.create_rectangle(20,100, 500,150, fill='white')
# canvas.create_rectangle(160,0, 210,250, fill='white')
# canvas.create_rectangle(20,110, 500,140, fill='blue')
# canvas.create_rectangle(170,0, 200,250, fill='blue')

# Senegal
# f = Flag(canvas, horizontal=False, colors=['green', 'yellow', 'red'], country_name='Senegal')
# s = Star(canvas, 260, 125, 40, color='green')

# Siria
# f = Flag(canvas, horizontal=True, colors=['red', 'white', 'black'], country_name='Siria')
# s = Star(canvas, 200, 125, 30, color='green')
# s = Star(canvas, 320, 125, 30, color='green')

# Somalia
# f = Flag(canvas, horizontal=True, colors=['royal blue'], country_name='Somalia')
# s = Star(canvas, 260, 125, 50, color='white')

# Sudan
# f = Flag(canvas, horizontal=True, colors=['red', 'white', 'black'], country_name='Sudan')
# canvas.create_polygon(20,0, 140,125, 20,250, fill='green')

# Suedia
# f = Flag(canvas, horizontal=True, colors=['royal blue'], country_name='Suedia')
# canvas.create_rectangle(20,100, 500,150, fill='yellow')
# canvas.create_rectangle(160,0, 210,250, fill='yellow')

# Tanzania
# f = Flag(canvas, horizontal=True, colors=['yellow'], country_name='Tanzania')
# canvas.create_polygon(20,0, 440,0, 20,200, fill='green')
# canvas.create_polygon(85,250, 500,250, 500,50, fill='blue')
# canvas.create_polygon(20,215, 20,250, 55,250, 500,35, 500,0, 465,0, fill='black')

# Tonga
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Tonga')
# canvas.create_rectangle(20,0, 200,125, fill='white')
# canvas.create_rectangle(95,25, 125,100, fill='red', outline='red')
# canvas.create_rectangle(73,45, 147,75, fill='red', outline='red')

# Trinidad & Tobago
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Trinidad & Tobago')
# canvas.create_polygon(20,0, 150,0, 500,250, 350,250, fill='white')
# canvas.create_polygon(45,0, 125,0, 475,250, 375,250, fill='black')

# Palestina
# f = Flag(canvas, horizontal=True, colors=['black', 'white', 'green'], country_name='Palestina')
# canvas.create_polygon(20,0, 160,125, 20,250, fill='red')

# Vietnam
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Vietnam')
# s = Star(canvas, 260, 125, 50)

# Sfantul Vincent & Grenadine
# f = Flag(canvas, horizontal=True, colors=['yellow'], country_name='Sfantul Vincent & Grenadine')
# canvas.create_rectangle(20,0, 120,250, fill='blue')
# canvas.create_rectangle(400,0, 500,250, fill='green')
# canvas.create_polygon(200,125, 225,90, 250,125, 225,155, fill='green')
# canvas.create_polygon(270,125, 295,90, 320,125, 295,155, fill='green')
# canvas.create_polygon(235,170, 260,135, 285,170, 260,205, fill='green')

# Scotia
# f = Flag(canvas, horizontal=True, colors=['white'], country_name='Scotia')
# canvas.create_polygon(20,20, 180,125, 20,230, fill='royal blue')
# canvas.create_polygon(500,20, 340,125, 500,230, fill='royal blue')
# canvas.create_polygon(100,0, 260,100, 400,0, fill='royal blue')
# canvas.create_polygon(100,250, 260,150, 400,250, fill='royal blue')













# Greu
# Africa de Sud
# f = Flag(canvas, horizontal=True, colors=['red', 'white', 'blue'], country_name='Africa de Sud')
# canvas.create_rectangle(20,125-83/2, 500,125+83/2, fill='white')
# canvas.create_polygon(20,0, 100,0, 280,125, 100,250, 20,250, fill='white')
# canvas.create_rectangle(20,100, 500,150, fill='green')
# canvas.create_polygon(20,0, 80,0, 260,125, 80,250, 20,250, fill='green')
# canvas.create_polygon(20,20, 230,125, 20,230, fill='yellow')
# canvas.create_polygon(20,40, 200,125, 20,210, fill='black')

# Antigua & Barbuda
# f = Flag(canvas, horizontal=True, colors=['black', 'white'], country_name='Antigua & Barbuda')
# s = Star(canvas, 260,100,90,n=16)
# c = Circle(canvas, 260, 100, 50, color='yellow', outline='yellow')
# canvas.create_rectangle(20,100, 500,150, fill='blue')
# canvas.create_rectangle(20,150, 500,250, fill='white')
# canvas.create_polygon(20,0, 260,250, 20,250, fill='red')
# canvas.create_polygon(500,0, 260,250, 500,250, fill='red')

# Australia
# f = Flag(canvas, horizontal=True, colors=['blue'], country_name='Australia')
# canvas.create_polygon(20,0, 60,0, 260,125, 220,125, fill='white')
# canvas.create_polygon(20,125, 60,125, 260,0, 220,0, fill='white')
# canvas.create_polygon(30,0, 40,0, 250,125, 240,125, fill='red')
# canvas.create_polygon(30,125, 40,125, 250,0, 240,0, fill='red')
# canvas.create_rectangle(20,47, 260,77, fill='white', outline='white')
# canvas.create_rectangle(125,0, 155,125, fill='white', outline='white')
# canvas.create_rectangle(20,52, 260,72, fill='red', outline='red')
# canvas.create_rectangle(130,0, 150,125, fill='red', outline='red')
# S = Star(canvas, 140, 190, 30, 'white', 7)
# S = Star(canvas, 380, 40, 15, 'white', 7)
# S = Star(canvas, 420, 80, 15, 'white', 7)
# S = Star(canvas, 310, 110, 15, 'white', 7)
# S = Star(canvas, 380, 210, 15, 'white', 7)
# S = Star(canvas, 400, 125, 7, 'white', 5)

# Azerbadjan
# f = Flag(canvas, horizontal=True, colors=['cyan', 'red', 'green'], country_name='Azerbadjan')
# c = Circle(canvas, 260, 125, 40, color='white', outline='red')
# c = Circle(canvas, 270, 125, 35, color='red', outline='red')
# s = Star(canvas, 280, 125, 25, 'white', 8)

# Canada
# f = Flag(canvas, horizontal=False, colors=['white'], country_name='Canada')
# canvas.create_rectangle(20,0, 140,250, fill='red')
# canvas.create_rectangle(380,0, 500,250, fill='red')
#
# canvas.create_polygon(
#     265,230, 255,230,
#     255,180, 210,187,
#     215,170, 163,125,
#     176,120, 168,90,
#     197,96, 204,80,
#     231,106, 222,48,
#     241,56, 260,20,
#     279,56, 298,48,
#     290,100, 315,80,
#     324,96, 351,90,
#     343,120, 357,130,
#     305,170, 310,188,
#     265,180,
#     fill='red'
# )


# Comore
# f = Flag(canvas, horizontal=True, colors=['yellow', 'white', 'red', 'blue'], country_name='Comore')
# canvas.create_polygon(20,0, 220,125, 20,250, fill='green')
# c = Circle(canvas, 80, 125, 50, color='white', outline='green')
# c = Circle(canvas, 100, 125, 45, color='green', outline='green')
# s = Star(canvas, 100, 95, 10, color='white')
# s = Star(canvas, 100, 115, 10, color='white')
# s = Star(canvas, 100, 135, 10, color='white')
# s = Star(canvas, 100, 155, 10, color='white')

# Rep. Democratica Congo
# f = Flag(canvas, horizontal=True, colors=['yellow'], country_name='Rep. Democratica Congo')
# canvas.create_polygon(20,0, 20,200, 470,0, fill='royal blue')
# canvas.create_polygon(50,250, 500,250, 500,50, fill='royal blue')
# canvas.create_polygon(20,220, 20,250, 500,30, 500,0, fill='red')
# s = Star(canvas, 120, 65, 50)

# Coreea de Nord
# f = Flag(canvas, horizontal=True, colors=['royal blue'], country_name='Coreea de Nord')
# canvas.create_rectangle(20,40, 500,210, fill='white')
# canvas.create_rectangle(20,50, 500,200, fill='red')
# c = Circle(canvas, 200, 125, 50, 'white')
# s = Star(canvas, 200, 125, 50, 'red')

# Cuba
# f = Flag(canvas, horizontal=True, colors=['blue', 'white', 'blue', 'white', 'blue'], country_name='Cuba')
# canvas.create_polygon(20,0, 200,125, 20,250, fill='red')
# s = Star(canvas, 80, 125, 40, 'white')

# Djibouti
# f = Flag(canvas, horizontal=True, colors=['cyan', 'green'], country_name='Djibouti')
# canvas.create_polygon(20,0, 260,125, 20,250, fill='white')
# s = Star(canvas, 120, 125, 30, 'red')

# Etiopia
# f = Flag(canvas, horizontal=True, colors=['green', 'yellow', 'red'], country_name='Etiopia')
# c = Circle(canvas, 260, 125, 85, 'royal blue')
# canvas.create_polygon(260,60, 298,180,
#                       260,150, 220,180, fill='', outline='yellow',width='5')
#
# canvas.create_polygon(195,100, 320,100,
#                       260,150, fill='', outline='yellow',width='5')
#
# canvas.create_line(260,190, 260,160, fill='yellow',width='2')
# canvas.create_line(195,145, 230,135, fill='yellow',width='2')
# canvas.create_line(220,70, 243,95, fill='yellow',width='2')
# canvas.create_line(280,95, 305,70, fill='yellow',width='2')
# canvas.create_line(290,135, 323,145, fill='yellow',width='2')


# Grecia
# f = Flag(canvas, horizontal=True, colors= ['royal blue','white'] * 4 + ['royal blue'], country_name='Grecia')
# canvas.create_rectangle(20,0, 150,135, fill='royal blue', outline='royal blue')
# canvas.create_rectangle(73,0, 97,135, fill='white', outline='white')
# canvas.create_rectangle(20,55, 150,83, fill='white', outline='white')

# Guineea-Bissau
# f = Flag(canvas, horizontal=True, colors=['yellow', 'green'], country_name='Guineea-Bissau')
# canvas.create_rectangle(20,0, 150,250, fill='red', outline='red')
# s = Star(canvas, 85, 125, 30, 'black')

# Guyana
# f = Flag(canvas, horizontal=True, colors=['green'], country_name='Guyana')
# canvas.create_polygon(20,0, 500,125, 20,250, fill='white')
# canvas.create_polygon(20,10, 450,125, 20,240, fill='yellow')
# canvas.create_polygon(20,0, 260,125, 20,250, fill='black')
# canvas.create_polygon(20,10, 240,125, 20,240, fill='red')

# Iordania
# f = Flag(canvas, horizontal=True, colors=['black', 'white', 'green'], country_name='Iordania')
# canvas.create_polygon(20,0, 200,125, 20,250, fill='red')
# s = Star(canvas, 80, 125, 15, 'white', 7)

# Honduras
# f = Flag(canvas, horizontal=True, colors=['blue', 'white', 'blue'], country_name='Honduras')
# s = Star(canvas, 260,125,10,'blue')
# s = Star(canvas, 220,105,10,'blue')
# s = Star(canvas, 220,145,10,'blue')
# s = Star(canvas, 300,105,10,'blue')
# s = Star(canvas, 300,145,10,'blue')

# Izrael
# f = Flag(canvas, horizontal=True, colors=['white'], country_name='Izrael')
# canvas.create_rectangle(20,0, 500,50, fill='blue')
# canvas.create_rectangle(20,200, 500,250, fill='blue')
# canvas.create_polygon(260,95, 220,155, 300,155, fill='', outline='blue', width=5)
# canvas.create_polygon(260,175, 220,115, 300,115, fill='', outline='blue', width=5)

# Liberia
# f = Flag(canvas, horizontal=True, colors=['red', 'white']*5+['red'], country_name='Liberia')
# canvas.create_rectangle(20,0, 150,109, fill='blue')
# s = Star(canvas, 85, 55, 30, 'white')

# Libia
# f = Flag(canvas, horizontal=True, colors=['black'], country_name='Libia')
# canvas.create_rectangle(20,0, 500,60, fill='red')
# canvas.create_rectangle(20,250, 500,190, fill='green')
# c = Circle(canvas, 260,125,40,'white')
# c = Circle(canvas, 265,125,37,'black')
# s = Star(canvas, 270, 125, 25, 'white', 5, False, 0)

# Macedonia de Nord
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Macedonia de Nord')
# canvas.create_polygon(20,0, 100,0, 260,125, fill='yellow')
# canvas.create_polygon(230,0, 290,0, 260,125, fill='yellow')
# canvas.create_polygon(420,0, 500,0, 260,125, fill='yellow')
# canvas.create_polygon(500,100, 500,150, 260,125, fill='yellow')
# canvas.create_polygon(20,100, 20,150, 260,125, fill='yellow')
# canvas.create_polygon(20,250, 100,250, 260,125, fill='yellow')
# canvas.create_polygon(230,250, 290,250, 260,125, fill='yellow')
# canvas.create_polygon(420,250, 500,250, 260,125, fill='yellow')
# c = Circle(canvas, 260,125,40,color='red', outline='red')
# c = Circle(canvas, 260,125,35,color='yellow', outline='red')

# Maldive
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Maldive')
# canvas.create_rectangle(100,50, 420,200, fill='green')
# c = Circle(canvas, 260,125,40, 'white')
# c = Circle(canvas, 275,125,40, 'green', 'green')

# Maroc
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Maroc')
# canvas.create_polygon(260,140, 220,110, 300,110, fill='', outline='green', width=5)
# canvas.create_polygon(260,85, 235,155, 260,140, 285,155, fill='', outline='green', width=5)

# Micronezia
# f = Flag(canvas, horizontal=True, colors=['royal blue'], country_name='Micronezia')
# s = Star(canvas, 260, 50, 20, 'white')
# s = Star(canvas, 320, 125, 20, 'white', right=False, rotation=-math.pi/4)
# s = Star(canvas, 200, 125, 20, 'white', right=False, rotation=math.pi/4)
# s = Star(canvas, 260, 200, 20, 'white', right=False)

# Namibia
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Namibia')
# canvas.create_polygon(20,0, 400,0, 20,200, fill='blue')
# canvas.create_line(20,200, 400,0, fill='white', width=5)
# canvas.create_polygon(120,250, 500,250, 500,50, fill='green')
# canvas.create_line(120,250, 500,50, fill='white', width=5)
# s = Star(canvas, 100,67,40, 'yellow', 12)
# c = Circle(canvas, 100,67,20, 'blue', outline='yellow')
# c = Circle(canvas, 100,67,17, 'yellow', outline='yellow')

# Nauru
# f = Flag(canvas, horizontal=True, colors=['blue'], country_name='Nauru')
# canvas.create_rectangle(20,115, 500,135, fill='yellow')
# s = Star(canvas, 130, 175, 30, 'white', 12)

# Pakistan
# f = Flag(canvas, horizontal=False, colors=['white', 'green', 'green'], country_name='Pakistan')
# c = Circle(canvas, 340, 125, 70, 'white', 'green')
# c = Circle(canvas, 360, 110, 60, 'green', 'green')
# s = Star(canvas, 370,100,25,'white',5,False,rotation=math.pi/3)

# Panama
# f = Flag(canvas, horizontal=False, colors=['blue', 'red'], country_name='Panama')
# canvas.create_rectangle(20,0, 260,125, fill='white')
# canvas.create_rectangle(260,125, 500,250, fill='white')
# s = Star(canvas, 140,67,25,'blue')
# s = Star(canvas, 380,192,25,'red')

# Qatar
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Qatar')
# canvas.create_polygon(20,0, 150,0,
#                       180,10,150,20, 180,30,150,40, 180,50,150,60, 180,70,150,80,
#                       180,90,150,100, 180,110,150,120, 180,130,150,140, 180,150,150,160,
#                       180,170,150,180, 180,190,150,200, 180,210,150,220, 180,230,150,240,
#                       180,250, 20,250, fill='white')

# Regatul Unit al Marii Britanii
# f = Flag(canvas, horizontal=True, colors=['blue'], country_name='Regatul Unit al Marii Britanii')
# canvas.create_polygon(20,0, 20,30, 500,250, 500,220, fill='white')
# canvas.create_polygon(20,250, 20,220, 500,0, 500,30, fill='white')
# canvas.create_polygon(20,10, 20,20, 500,240, 500,230, fill='red')
# canvas.create_polygon(20,240, 20,230, 500,10, 500,20, fill='red')
# canvas.create_rectangle(20,100, 500,150, fill='white', outline='white')
# canvas.create_rectangle(240,0, 280,250, fill='white', outline='white')
# canvas.create_rectangle(20,110, 500,140, fill='red', outline='red')
# canvas.create_rectangle(250,0, 270,250, fill='red', outline='red')

# Samoa
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Samoa')
# canvas.create_rectangle(20,0, 260,125, fill='blue')
# s = Star(canvas, 140,20,12,'white')
# s = Star(canvas, 170,40,10,'white')
# s = Star(canvas, 100,50,10,'white')
# s = Star(canvas, 160,70,7,'white')
# s = Star(canvas, 140,100,12,'white')

# Sao Tome & Principe
# f = Flag(canvas, horizontal=True, colors=['green', 'yellow', 'green'], country_name='Sao Tome & Principe')
# canvas.create_polygon(20,0, 120,125, 20,250, fill='red')
# s = Star(canvas, 260,125,30,'black')
# s = Star(canvas, 350,125,30,'black')

# Sf. Kitts & Nevis
# f = Flag(canvas, horizontal=True, colors=['black'], country_name='Sf. Kitts & Nevis')
# canvas.create_polygon(20,0, 400,0, 20,200, fill='green')
# canvas.create_line(20,200, 400,0, fill='yellow', width=10)
# canvas.create_polygon(120,250, 500,250, 500,50, fill='red')
# canvas.create_line(120,250, 500,50, fill='yellow', width=10)
# s = Star(canvas, 180,172,40,'white',5,False,math.pi/180*-10)
# s = Star(canvas, 340,85,40,'white',5,False,math.pi/180*-10)

# Seychelles
# f = Flag(canvas, horizontal=True, colors=['red'], country_name='Seychelles')
# canvas.create_polygon(20,0, 180,0, 20,250, fill='blue')
# canvas.create_polygon(180,0, 340,0, 20,250, fill='yellow')
# canvas.create_polygon(500,83, 500,166, 20,250, fill='white')
# canvas.create_polygon(500,166, 500,250, 20,250, fill='green')

# Sf. Lucia
# f = Flag(canvas, horizontal=True, colors=['royal blue'], country_name='Sf. Lucia')
# canvas.create_polygon(200,230, 320,230, 260,20, fill='white')
# canvas.create_polygon(210,230, 310,230, 260,40, fill='black')
# canvas.create_polygon(200,230, 320,230, 260,125, fill='yellow')


# Singapore
# f = Flag(canvas, horizontal=True, colors=['red', 'white'], country_name='Singapore')
# canvas.create_line(20,250, 500,250, fill='black')
# c = Circle(canvas, 120, 67, 50, 'white', 'white')
# c = Circle(canvas, 140, 67, 50, 'red', 'red')
# s = Star(canvas, 140, 40, 10, 'white')
# s = Star(canvas, 120, 60, 10, 'white')
# s = Star(canvas, 160, 60, 10, 'white')
# s = Star(canvas, 125, 85, 10, 'white')
# s = Star(canvas, 155, 85, 10, 'white')

# Insulele Solomon
# f = Flag(canvas, colors=['yellow'], country_name='Insulele Solomon')
# canvas.create_polygon(20,0, 450,0, 20,230, fill='royal blue')
# canvas.create_polygon(50,250, 500,250, 500,0, fill='green')
# s = Star(canvas, 60, 40, 20, color='white')
# s = Star(canvas, 180, 40, 20, color='white')
# s = Star(canvas, 120, 80, 20, color='white')
# s = Star(canvas, 60, 120, 20, color='white')
# s = Star(canvas, 180, 120, 20, color='white')

# Sudanul de Sud
# f = Flag(canvas, horizontal=True, colors=['black', 'red', 'green'], country_name='Sudanul de Sud')
# canvas.create_line(20,83, 500,83, fill='white', width=8)
# canvas.create_line(20,166, 500,166, fill='white', width=8)
# canvas.create_polygon(20,0, 250,125, 20,250, fill='royal blue')
# s = Star(canvas,  120,125, 50, right=False, rotation=-math.pi/9)

# Surinam
# f = Flag(canvas, horizontal=True, colors=['green', 'red', 'green'], country_name='Surinam')
# canvas.create_line(20,73, 500,73, fill='white', width=20)
# canvas.create_line(20,175, 500,175, fill='white', width=20)
# s = Star(canvas, 260,125,40)

# Timorul de Est
# f = Flag(canvas, colors=['red'], country_name='Timorul de Est')
# canvas.create_polygon(20,0, 250,125, 20,250, fill='yellow')
# canvas.create_polygon(20,0, 150,125, 20,250, fill='black')
# s = Star(canvas, 70,125,30, color='white',right=False)

# Togo
# f = Flag(canvas, horizontal=True, colors=['green','orange','green','orange','green'], country_name='Togo')
# canvas.create_rectangle(20,0, 170,150, fill='red', outline='red')
# s = Star(canvas, 95,75,50,'white')

# Tunisia
# f = Flag(canvas, colors=['red'], country_name='Tunisia')
# c = Circle(canvas, 260,125,70,'white', 'red')
# c = Circle(canvas, 260,125,50,'red', 'red')
# c = Circle(canvas, 270,125,43,'white', 'white')
# s = Star(canvas, 270, 125, 30, 'red', right=False)

# Turcia
# f = Flag(canvas, colors=['red'], country_name='Turcia')
# c = Circle(canvas, 200,125,80,'white', 'red')
# c = Circle(canvas, 225,125,60,'red', 'red')
# s = Star(canvas, 290,125,30,'white',right=False)






# Mainloop
root.mainloop()