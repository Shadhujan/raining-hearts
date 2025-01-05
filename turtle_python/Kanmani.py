import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("sky blue")  # Set the background color to sky blue

# Create a turtle object
pen = turtle.Turtle()
pen.speed(1)

# Function to draw a heart
def draw_heart():
    pen.color("red")
    pen.fillcolor("red")
    pen.penup()
    pen.goto(0, -50)
    pen.pendown()
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

# Function to draw a letter
def draw_letter(letter, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.write(letter, font=("Arial", 48, "normal"))

# Function to draw the name 'Janudi'
def draw_name():
    pen.color("black")
    name = "Janudi"
    x_start = -150
    y_start = 0
    spacing = 60

    for i, letter in enumerate(name):
        draw_letter(letter, x_start + i * spacing, y_start)

# Function to draw the text 'your's booboo'
def draw_text():
    pen.penup()
    pen.goto(-200, -200)
    pen.pendown()
    pen.write("your's booboo😘", font=("Arial", 18, "normal"))

# Draw everything
draw_heart()
draw_name()
draw_text()

# Function to create a falling heart effect
hearts = []
for _ in range(20):  # Increase the number of hearts
    heart = turtle.Turtle()
    heart.penup()
    heart.hideturtle()
    heart.goto(random.randint(-300, 300), random.randint(100, 300))
    hearts.append(heart)

def move_hearts():
    for heart in hearts:
        heart.clear()
        heart.sety(heart.ycor() - 15)  # Increase falling speed
        heart.write('❤️', align="center", font=("Arial", 24, "normal"))
        if heart.ycor() < -300:
            heart.clear()
            heart.goto(random.randint(-300, 300), random.randint(100, 300))
    screen.ontimer(move_hearts, 30)  # Reduce timer interval for faster appending

# Start the falling hearts effect
move_hearts()

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()
