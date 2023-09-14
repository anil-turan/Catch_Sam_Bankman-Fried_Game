import turtle
from turtle import Shape
from turtle import *
import random
global posit
screen = turtle.Screen()
ima = r"asd123.gif"
#screen.register_shape(ima, ((5,-3), (0,5), (-5,-3)))
screen.addshape(name=ima,shape=None)
screen.bgcolor("light blue")
screen.title("Catch Sam Bankman-Fried")
FONT = ('Arial',30,'bold')
score = 0
game_over = False

turtle_list = []

score_turtle = turtle.Turtle()

countdown_turtle = turtle.Turtle()

#make turtle properties
grid_size = 15
x_coordinates = [-20,-10,0,10,20]
y_coordinates = [-20,-10,0,10]

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("black")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9

    score_turtle.setpos(0,y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

def handle_click(x,y):
        global posit
        print("object position=",posit)
        curx, cury = posit
        if curx-20 < x < curx+20 and cury-20 < y < cury+20:
            global score
            score += 1
            score_turtle.clear()
            score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)
            print("click position=",x,y)
            
 

def make_turtle(x,y):
    t = turtle.Turtle()
    t.penup()
    t.shape(ima)
    t.shapesize(3,3,outline=True)
    t.color("black")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def showdeneme(item):
    global posit
    posit=item.position()
    item.showturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        a=random.choice(turtle_list)
        showdeneme(a)
        screen.ontimer(show_turtles_randomly,500)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setpos(0,y - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)

def start_game_up():
    turtle.tracer(0)
    setup_turtles()
    setup_score_turtle()
    hide_turtles()
    show_turtles_randomly()
    countdown(30)
    turtle.tracer(1)

start_game_up()
turtle.onscreenclick(handle_click, btn=1, add=None)
turtle.mainloop()