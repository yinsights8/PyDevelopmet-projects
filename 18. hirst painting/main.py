# import colorgram
#
# colors = colorgram.extract("hirst.jpg", 30)

# total_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     total_color.append(new_color)
#
# print(total_color)

import turtle as t
import random

t.colormode(255)
# in order to use random color list (r,g,b) we need to reset the colormode. if not it's going to give an error
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176),
              (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49),
              (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86),
              (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162),
              (156, 212, 190), (87, 46, 33), (37, 45, 83)]


tim = t.Turtle()
tim.penup()
tim.hideturtle()
# t.bgcolor("black")
number_of_dots = 100
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")

for steps in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if steps % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
