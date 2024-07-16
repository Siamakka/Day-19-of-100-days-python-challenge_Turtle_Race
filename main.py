from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width= 500, height= 400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# turtles = ["tim", "tom", "abbas", "jafar", "siamak", "taghi"]

is_race_on = False

user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will wni the race? Enter a color:\nRed\nOrange\nYellow\nGreen\nBlue\nPurple")

all_turtles = []

y = -70

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.up()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y)
    y += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False

            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)










screen.exitonclick()