"""
Created on Fri May 14 22:22:14 2020

@email_id : shubham.more26@gmail.com
@author: SHUBHAM MORE
"""

import turtle
from turtle import *

height = 750
width = 1500
screen = Screen()
screen.setup(width, height)



t = turtle

t.speed(100)
t.up()
t.speed(20)
t.lt(1)

t.color("#ffff00")
t.pencolor("black")
t.lt(50)
t.fd(120)  # start point
t.begin_fill()

t.down()
t.circle(120, 60)
t.rt(4)
t.fd(70)
t.rt(4)
t.fd(20)
t.rt(100)
t.fd(40)
t.circle(340, 30)
t.lt(130)
t.circle(330, 41)
t.rt(70)
t.circle(170, 97)
t.rt(70)
t.circle(330, 40)
t.lt(130)
t.circle(500, 25)
t.rt(110)
t.circle(120, 30)
t.fd(10)
t.circle(280, 10)
t.circle(170, 15)
t.lt(15)
t.circle(240, 40)
t.lt(1)
t.circle(240, 15)
t.lt(13)
t.circle(240, 24)

t.end_fill()
t.up()
t.lt(60)
t.fd(140)
t.down()
t.color("black")  # R_eye

t.begin_fill()
t.circle(30)
t.end_fill()

t.lt(45)
t.fd(35)
t.color("white")
t.pencolor("black")
t.begin_fill()
t.circle(15)
t.end_fill()
t.lt(25)

t.color("black")  # R_eye

t.begin_fill()

t.up()
t.fd(150)
t.down()
t.circle(30)  # L_eye
t.end_fill()
t.end_fill()

t.color("white")
t.pencolor("black")
t.begin_fill()
t.circle(15)
t.end_fill()

# -----------------------------------------------------face--------------------


t.up()
t.lt(100)
t.fd(125)
t.lt(30)
t.down()
###
t.circle(10, 5)
t.lt(15)
t.circle(60, 20)

t.fd(20)
t.up()
turtle.fd(158)
t.rt(60)
t.down()
############body

t.color("yellow")  # R_eye
t.pencolor("black")
t.begin_fill()

t.circle(-450, 25)
t.rt(10)
t.fd(20)
t.lt(22)
t.circle(50, 10)
t.circle(50, 10)
t.rt(22)
t.circle(50, 10)
t.circle(50, 10)
t.circle(50, 10)
t.rt(22)
t.circle(50, 20)
t.rt(20)
t.fd(20)

t.circle(-300, 20)
t.rt(15)
#
t.circle(20, 2)
t.circle(20, 0)

t.circle(20, 0)
t.fd(10)
t.rt(30)
t.circle(40, 5)
t.fd(20)

t.circle(-40, 15)
t.fd(40)
t.circle(-40, 15)

t.fd(20)
t.circle(-40, 40)
t.fd(20)

t.circle(-30, 20)
t.lt(70)
t.rt(1)
t.circle(-300, 30)
t.rt(30)
t.circle(30, 30)
t.rt(30)
t.fd(50)

t.rt(30)
t.fd(50)
t.rt(30)
t.fd(70)
t.rt(20)
t.fd(50)

t.rt(20)
t.fd(10)
t.lt(20)

# t.clone()
t.lt(40)
t.circle(-380, 40)
t.end_fill()

t.rt(100)
t.circle(300, 30)
t.lt(21)

t.circle(300, 25)
t.up()

# t.fd(20)
t.down()

t.color("red")
t.pencolor("black")
t.begin_fill()
t.lt(20)
t.up()
t.fd(32)
t.rt(+22)
t.down()
t.circle(35)
t.end_fill()
t.up()
t.lt(132)
t.fd(269)
t.down()
t.color("red")
t.pencolor("black")
t.begin_fill()
t.circle(35)
t.end_fill()

t.pencolor("YELLOW")
t.color("yellow")
t.begin_fill()

t.backward(109)
t.circle(52)
t.end_fill()

t.pencolor("black")

t.lt(7)
t.back(15)
t.rt(45)
t.fd(15)
t.lt(107)
t.fd(14)
t.up()
t.fd(60)
t.rt(45)
t.back(100)
t.down()
t.lt(60)
t.circle(-18, 130)
t.lt(25)
t.circle(32, 80)
t.rt(20)
t.circle(-20, 90)
t.up()
t.fd(29)

# -------------------------------------------
# t.pencolor ("black")
# t.color ("yellow")
t.begin_fill()

t.circle(14)
t.end_fill()
t.down()
t.pencolor("black")
t.up()
t.lt(30)
t.fd(280)

t.begin_fill()
t.color("black")
t.rt(45)
t.down()
t.fd(55)
t.lt(85)
t.circle(280, 20)
t.end_fill()

# -----------------
t.rt(23)
t.up()
t.back(660)
t.lt(90)
t.begin_fill()
t.color("black")
t.down()
t.fd(53)
t.lt(100)
t.circle(300, 20)

t.end_fill()
t.up()
t.lt(3)
t.back(660)
t.down()
t.rt(90)
t.circle(450, 15)
t.circle(90, 30)
t.lt(120)
t.fd(10)
t.rt(120)
t.fd(10)
t.lt(120)
t.fd(10)
t.rt(120)
t.fd(10)

t.lt(120)
t.fd(10)
t.rt(120)
t.fd(10)
t.lt(120)
t.fd(10)

t.circle(450, 27)
t.up()
t.lt(37)
t.back(290)
t.lt(40)
t.down()
t.circle(450, 22)

t.circle(90, 30)
t.lt(120)
t.fd(10)
t.rt(120)
t.fd(10)
t.lt(120)
t.fd(10)
t.rt(120)
t.fd(10)

t.lt(120)
t.fd(10)
t.rt(120)
t.fd(10)
t.lt(117)
t.fd(10)
t.lt(8)
t.circle(430, 20)  # r hand down side
t.up()
t.back(30)
t.rt(120)
t.fd(44)
t.down()
# --------------------------------------------------
t.begin_fill()
t.lt(70)
t.color("yellow")
t.pencolor("black")
t.circle(-400, 5)
t.lt(110)
t.circle(-400, 15)
t.rt(70)
t.circle(-400, 20)
t.lt(110)
t.circle(-400, 25)
t.rt(60)
t.circle(-500, 35)

t.rt(110)
t.circle(-500, 17)

t.rt(20)
t.circle(-500, 10)
t.lt(90)
t.circle(-500, 17)

t.rt(80)
t.circle(-500, 21)

t.lt(110)
t.circle(-450, 15)
t.rt(80)
t.circle(-500, 11)

t.end_fill()
t.begin_fill()

t.color("brown")
t.pencolor("black")
t.lt(180)
t.circle(550.5, 10)
t.lt(82)
t.circle(550, 12)
t.lt(145)
t.circle(550, 3)

t.rt(145)
t.circle(550, 1)
t.lt(145)
t.circle(550, 2)
t.rt(145)
t.circle(550, 3)
t.lt(145)
t.circle(550, 2)
t.rt(145)
t.circle(300, 2)
t.lt(145)
t.circle(550, 2)
t.rt(145)
t.circle(300, 2)
t.circle(300, 2)
t.lt(145)
t.circle(300, 2)
t.rt(145)
t.circle(300, 5)
t.lt(159)
t.circle(600, 6)
t.rt(110)
t.circle(300, 8)
t.lt(85)
t.circle(300, 3)
t.fd(30)
t.up()
t.end_fill()
t.fd(90)

t.color("brown")
t.pencolor("black")

turtle.getscreen()._root.mainloop()
