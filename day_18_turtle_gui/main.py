import turtle
from turtle import Turtle, Screen
import random
import colorgram


colors = ['CornflowerBlue','DarkOrchid','DeepSkyBlue','IndianRed','LightSeaGreen','ForestGreen', "wheat", "SlateGray"]
colors_extracted = [(153, 91, 49), (209, 156, 107), (42, 111, 146), (60, 116, 75), (199, 157, 31), (240, 58, 34), (131, 170, 183), (248, 211, 75), (155, 7, 26), (145, 64, 87), (146, 219, 161), (29, 178, 108), (188, 132, 139), (253, 232, 0), (125, 181, 123), (23, 55, 82), (222, 49, 52), (193, 234, 198), (46, 151, 194), (17, 90, 59), (250, 147, 138), (3, 78, 45), (250, 146, 159), (218, 231, 237), (192, 26, 13), (3, 82, 118), (81, 71, 41), (46, 62, 86)]

tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.color("SlateBlue2")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
def drawSquare():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

def drawShapes():
    for i in range(3, 11):
        sides = i
        tim.color(random.choice(colors))
        for _ in range(0, sides):
            degrees = 360 / sides
            tim.forward(100)
            tim.right(degrees)

def randomWalk():
    angle = [0, 90, 180, 270]
    tim.pensize(10)
    tim.speed('fast')
    for _ in range(100):
        tim.color(random_color())
        tim.setheading(random.choice(angle))
        tim.forward(30)

def drawSpirograph(size):
    tim.speed('fastest')
    for _ in range(size):
        tim.color(random_color())
        tim.circle(100)
        tim.left(360/size)

def getColorsFromImage():
    list_of_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        list_of_colors.append((r, g, b))
    print(list_of_colors)

def hirstPainting(dots):
    y_axis = -250
    number_of_dots = dots

    tim.hideturtle()
    tim.speed('fastest')
    tim.penup()

    for _ in range(number_of_dots):
        tim.setposition(-250, y_axis)
        y_axis += 50
        for _ in range(number_of_dots):
            dot_color = random.choice(colors_extracted)
            tim.dot(20, dot_color)
            tim.forward(50)



hirstPainting(10)

screen = Screen()
screen.exitonclick()