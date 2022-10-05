# import colorgram
#
#
# def rgb_from_pic(picture, num_of_colors):
#     colors = colorgram.extract(picture, num_of_colors)
#     color_list = []
#
#     for color in colors:
#         rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#         color_list.append(rgb)
#
#     return color_list
#
#
# rgb_colors = rgb_from_pic("image.jpg", 30)
#
# print(rgb_colors)
import turtle
from random import choice
from turtle import Turtle, Screen

color_list = [(229, 241, 234), (222, 145, 91), (117, 163, 216), (47, 102, 161), (243, 77, 34), (144, 63, 89),
              (241, 232, 235), (179, 57, 37), (244, 206, 73), (220, 229, 237), (48, 133, 64), (222, 121, 150),
              (229, 78, 100), (120, 198, 149), (192, 148, 52), (55, 166, 131), (127, 219, 187), (102, 103, 173),
              (55, 51, 129), (82, 45, 34), (245, 160, 148), (17, 103, 45), (63, 45, 56), (43, 31, 68), (253, 200, 0),
              (100, 90, 6), (125, 41, 48), (156, 216, 223), (231, 166, 178)]

tim = Turtle()
tim.shape("classic")
tim.speed(9)

screen = Screen()
screen.colormode(255)

tim.penup()
tim.goto(-250,-250)
for __ in range(10):

    for _ in range(10):
        # tim.pendown()
        tim.dot(20, choice(color_list))
        # tim.penup()
        tim.forward(50)
    print(f"heading {tim.heading()}")
    print(f"position {tim.pos()}")
    position_x = tim.pos()[0]
    position_y = tim.pos()[1]
    if tim.heading() == 0:
        tim.setheading(180)
        tim.goto(position_x -50, position_y + 50)
    else:
        tim.setheading(0)
        tim.goto(position_x + 50, position_y + 50)
screen.exitonclick()
