import turtle
import random

t = turtle.Turtle()
num = 100
t.left(90)
t.speed(0)
t.color("green")
t.screen.bgcolor("black")
t.pensize(2)

def tree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15)
        t.left(40)
        tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)

tree(num)
# Function to draw the name "Janudi"
def draw_name():
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.write("Janudi", font=("Arial", 24, "normal"))

# Function to draw a heart
def draw_heart():
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

# Draw the name and the heart
draw_name()
draw_heart()

turtle.done()