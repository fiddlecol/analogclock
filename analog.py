import turtle
import datetime
import math


def draw_roman_numeral(t, numeral, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.write(numeral, align="center", font=("Arial", 12, "normal"))


def draw_clock_hands():
    now = datetime.datetime.now()

    # Hour hand
    hour_angle = 90 - (now.hour % 12) * 30 - now.minute / 2
    hour_hand.setheading(hour_angle)
    hour_hand.pendown()

    # Minute hand
    minute_angle = 90 - now.minute * 6
    minute_hand.setheading(minute_angle)
    minute_hand.pendown()

    # Second hand
    second_angle = 90 - now.second * 6
    second_hand.setheading(second_angle)
    second_hand.pendown()

    # Update Roman numerals
    clock_face.clear()
    for i in range(1, 13):
        angle = 90 - i * 30
        x = 180 * math.cos(math.radians(angle))
        y = 180 * math.sin(math.radians(angle))
        draw_roman_numeral(clock_face, get_roman_numeral(i), (x, y))


def draw_clock_circle():
    circle_turtle.clear()
    circle_turtle.penup()
    circle_turtle.goto(0, -205)
    circle_turtle.pendown()
    circle_turtle.circle(205)


def update_clock():
    draw_clock_hands()
    draw_clock_circle()
    turtle.ontimer(update_clock, 1000)  # Update every 1000 milliseconds (1 second)


def get_roman_numeral(number):
    roman_numerals = ["XII", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
    return roman_numerals[number]


# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("grey")
screen.title("Analog Clock")

# Create the clock face
clock_face = turtle.Turtle()
clock_face.speed(0)  # Fastest speed
clock_face.color("black")
clock_face.hideturtle()

# Draw the clock circle
clock_face.penup()
clock_face.goto(0, -200)
clock_face.pendown()
clock_face.circle(200)

# Create the clock hands
hour_hand = turtle.Turtle()
hour_hand.speed(0)
hour_hand.color("black")
hour_hand.pensize(10)
hour_hand.shape("arrow")
hour_hand.shapesize(stretch_wid=0.5, stretch_len=8)
hour_hand.penup()

minute_hand = turtle.Turtle()
minute_hand.speed(0)
minute_hand.color("green")
minute_hand.pensize(5)
minute_hand.shape("arrow")
minute_hand.shapesize(stretch_wid=0.3, stretch_len=12)
minute_hand.penup()

second_hand = turtle.Turtle()
second_hand.speed(0)
second_hand.color("black")
second_hand.pensize(2)
second_hand.shape("arrow")
second_hand.shapesize(stretch_wid=0.05, stretch_len=16)
second_hand.penup()

# Create a turtle for the clock circle
circle_turtle = turtle.Turtle()
circle_turtle.speed(0)
circle_turtle.hideturtle()
circle_turtle.color("blue")


# Start updating the clock
update_clock()

turtle.mainloop()
