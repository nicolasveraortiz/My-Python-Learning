import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S Game")
image = "blank_states_img.gif"
screen.addshape(image)

luis = turtle.Turtle()
luis.shape(image)
luis.penup()

chords = []
data = pandas.read_csv("50_states.csv")
countries = data["state"].tolist()
counter = 0
guesses = 0
for b in data["x"]:
    if b != "x":
        x = b
        y = data["y"][counter]
        chords.append((x, y))
        counter += 1

game_is_on = True
while game_is_on:
    screen.update()
    answer = screen.textinput(title=f"{guesses}/50 states", prompt="What's the another state?").title()
    if answer in countries:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        index = countries.index(answer)
        t.goto(chords[index])
        t.write(f"{countries[index]}")
        countries.pop(index)  # pop es una funcion que funciona con index, remove funciona con nombres de la lista
        chords.pop(index)
        guesses += 1
        if guesses == 50:
            print("You Win!!!")
            game_is_on = False

    elif answer == "Stop":
        game_is_on = False

screen.exitonclick()
