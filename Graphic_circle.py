# Made By falopr
from tkinter import *
import turtle

rad = 150


def submit_pressed():
    if en1.get() == '':
        en1.insert(0, '0')
    if en2.get() == '':
        en2.insert(0, '0')
    if en3.get() == '':
        en3.insert(0, '0')
    if en4.get() == '':
        en4.insert(0, '0')
    if en5.get() == '':
        en5.insert(0, '0')
    if en6.get() == '':
        en6.insert(0, '0')
    if en7.get() == '':
        en7.insert(0, '0')
    if en8.get() == '':
        en8.insert(0, '0')
    if en9.get() == '':
        en9.insert(0, '0')
    if en10.get() == '':
        en10.insert(0, '0')

    var1 = int(en1.get())
    var2 = int(en2.get())
    var3 = int(en3.get())
    var4 = int(en4.get())
    var5 = int(en5.get())
    var6 = int(en6.get())
    var7 = int(en7.get())
    var8 = int(en8.get())
    var9 = int(en9.get())
    var10 = int(en10.get())

    step1 = var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10

    global percent1
    global percent2
    global percent3
    global percent4
    global percent5
    global percent6
    global percent7
    global percent8
    global percent9
    global percent10
    percentb1 = var1 / step1
    percent1 = percentb1 * 100
    percentb2 = var2 / step1
    percent2 = percentb2 * 100
    percentb3 = var3 / step1
    percent3 = percentb3 * 100
    percentb4 = var4 / step1
    percent4 = percentb4 * 100
    percentb5 = var5 / step1
    percent5 = percentb5 * 100
    percentb6 = var6 / step1
    percent6 = percentb6 * 100
    percentb7 = var7 / step1
    percent7 = percentb7 * 100
    percentb8 = var8 / step1
    percent8 = percentb8 * 100
    percentb9 = var9 / step1
    percent9 = percentb9 * 100
    percentb10 = var10 / step1
    percent10 = percentb10 * 100

    step2 = 360 / step1
    window.destroy()

    global varb1
    global varb2
    global varb3
    global varb4
    global varb5
    global varb6
    global varb7
    global varb8
    global varb9
    global varb10
    varb1 = var1 * step2
    varb2 = var2 * step2
    varb3 = var3 * step2
    varb4 = var4 * step2
    varb5 = var5 * step2
    varb6 = var6 * step2
    varb7 = var7 * step2
    varb8 = var8 * step2
    varb9 = var9 * step2
    varb10 = var10 * step2


window = Tk()

window.geometry('300x240')
window.resizable(False, False)
window.title('Graphic Circle')
window.config(bg='#525252')

btn_sub = Button(window, width=10, relief='flat', text='Submit',
                 command=lambda: submit_pressed())
btn_sub.pack(side=BOTTOM, pady=10)

frame1 = Frame(window, bg='#525252')
frame1.pack(side=LEFT, anchor='nw')

frame2 = Frame(window, bg='#525252')
frame2.pack(side=RIGHT, anchor='ne')

en1 = Entry(frame1, relief='flat')
en1.pack(padx=10, pady=10)

en2 = Entry(frame1, relief='flat')
en2.pack(padx=10, pady=10)

en3 = Entry(frame1, relief='flat')
en3.pack(padx=10, pady=10)

en4 = Entry(frame1, relief='flat')
en4.pack(padx=10, pady=10)

en5 = Entry(frame1, relief='flat')
en5.pack(padx=10, pady=10)

en6 = Entry(frame2, relief='flat')
en6.pack(padx=10, pady=10)

en7 = Entry(frame2, relief='flat')
en7.pack(padx=10, pady=10)

en8 = Entry(frame2, relief='flat')
en8.pack(padx=10, pady=10)

en9 = Entry(frame2, relief='flat')
en9.pack(padx=10, pady=10)

en10 = Entry(frame2, relief='flat')
en10.pack(padx=10, pady=10)

window.mainloop()

tur_settings = turtle.Screen()
tur_settings.setup(width=0.8, height=0.8)
falopr = turtle.Turtle()
falopr.speed(100)

falopr.fillcolor('green')
falopr.begin_fill()
falopr.setheading(270)
falopr.forward(rad)
falopr.home()
falopr.setheading((270 + varb1))
falopr.forward(rad)
falopr.home()
falopr.up()
falopr.sety(-150)
falopr.circle(rad, varb1)
falopr.home()
falopr.down()
falopr.end_fill()

if varb2 != 0:
    falopr.fillcolor('blue')
    falopr.begin_fill()
    falopr.setheading((270 + varb1 + varb2))
    falopr.forward(rad)
    falopr.home()
    falopr.setheading((270 + varb1))
    falopr.forward(rad)
    falopr.setheading(270 + 90 + varb1)
    falopr.circle(rad, varb2)
    falopr.end_fill()

if varb3 != 0:
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3))
    falopr.fillcolor('yellow')
    falopr.begin_fill()
    falopr.forward(rad)
    falopr.home()
    falopr.setheading((270 + varb1 + varb2))
    falopr.forward(rad)
    falopr.setheading(270 + 90 + varb1 + varb2)
    falopr.circle(rad, varb3)
    falopr.end_fill()

if varb4 != 0:
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4))
    falopr.fillcolor('orange')
    falopr.begin_fill()
    falopr.forward(rad)
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3))
    falopr.forward(rad)
    falopr.setheading(270 + 90 + varb1 + varb2 + varb3)
    falopr.circle(rad, varb4)
    falopr.end_fill()

if varb5 != 0:
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4 + varb5))
    falopr.fillcolor('red')
    falopr.begin_fill()
    falopr.forward(rad)
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4))
    falopr.forward(rad)
    falopr.setheading(270 + 90 + varb1 + varb2 + varb3 + varb4)
    falopr.circle(rad, varb5)
    falopr.end_fill()

if varb6 != 0:
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6))
    falopr.fillcolor('cyan')
    falopr.begin_fill()
    falopr.forward(rad)
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4 + varb5))
    falopr.forward(rad)
    falopr.setheading(270 + 90 + varb1 + varb2 + varb3 + varb4 + varb5)
    falopr.circle(rad, varb6)
    falopr.end_fill()

if varb7 != 0:
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6 + varb7))
    falopr.fillcolor('black')
    falopr.begin_fill()
    falopr.forward(rad)
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6))
    falopr.forward(rad)
    falopr.setheading(270 + 90 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6)
    falopr.circle(rad, varb7)
    falopr.end_fill()

if varb8 != 0:
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6 + varb7 + varb8))
    falopr.fillcolor('purple')
    falopr.begin_fill()
    falopr.forward(rad)
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6 + varb7))
    falopr.forward(rad)
    falopr.setheading(270 + 90 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6 + varb7)
    falopr.circle(rad, varb8)
    falopr.end_fill()

if varb9 != 0:
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6 + varb7 + varb8 + varb9))
    falopr.fillcolor('pink')
    falopr.begin_fill()
    falopr.forward(rad)
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6 + varb7 + varb8))
    falopr.forward(rad)
    falopr.setheading(270 + 90 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6 + varb7 + varb8)
    falopr.circle(rad, varb9)
    falopr.end_fill()

if varb10 != 0:
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6 + varb7 + varb8 + varb9 + varb10))
    falopr.fillcolor('white')
    falopr.begin_fill()
    falopr.forward(rad)
    falopr.home()
    falopr.setheading((270 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6 + varb7 + varb8 + varb9))
    falopr.forward(rad)
    falopr.setheading(270 + 90 + varb1 + varb2 + varb3 + varb4 + varb5 + varb6 + varb7 + varb8 + varb9)
    falopr.circle(rad, varb10)
    falopr.end_fill()

falopr.up()
falopr.home()
falopr.sety(-150)
falopr.circle(rad)
falopr.hideturtle()
falopr.sety(300)
falopr.setx(-350)
falopr.write('Green (1): ' + (str(varb1) + '°   ') + (str(percent1) + '%'), font=("Verdana",
                                    15, "normal"))
falopr.sety(270)
falopr.setx(-350)
falopr.write('Blue (2): ' + (str(varb2) + '°   ') + (str(percent2) + '%'), font=("Verdana",
                                    15, "normal"))
falopr.sety(240)
falopr.setx(-350)
falopr.write('Yellow (3): ' + (str(varb3) + '°   ') + (str(percent3) + '%'), font=("Verdana",
                                    15, "normal"))
falopr.sety(210)
falopr.setx(-350)
falopr.write('Orange (4): ' + (str(varb4) + '°   ') + (str(percent4) + '%'), font=("Verdana",
                                    15, "normal"))
falopr.sety(180)
falopr.setx(-350)
falopr.write('Red (5): ' + (str(varb5) + '°   ') + (str(percent5) + '%'), font=("Verdana",
                                    15, "normal"))
falopr.sety(-180)
falopr.setx(-350)
falopr.write('Cyan (6): ' + (str(varb6) + '°   ') + (str(percent6) + '%'), font=("Verdana",
                                    15, "normal"))
falopr.sety(-210)
falopr.setx(-350)
falopr.write('Black (7): ' + (str(varb7) + '°   ') + (str(percent7) + '%'), font=("Verdana",
                                    15, "normal"))
falopr.sety(-240)
falopr.setx(-350)
falopr.write('Purple (8): ' + (str(varb8) + '°   ') + (str(percent8) + '%'), font=("Verdana",
                                    15, "normal"))
falopr.sety(-270)
falopr.setx(-350)
falopr.write('Pink (9): ' + (str(varb9) + '°   ') + (str(percent9) + '%'), font=("Verdana",
                                    15, "normal"))
falopr.sety(-300)
falopr.setx(-350)
falopr.write('White (10): ' + (str(varb10) + '°   ') + (str(percent10) + '%'), font=("Verdana",
                                    15, "normal"))
turtle.done()
