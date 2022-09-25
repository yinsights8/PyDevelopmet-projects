import turtle
import pandas


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("India states Game")
image = "india.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("India States.csv")
data_list = data.States.to_list()
guesses = []
length = len(guesses)

while length < 36:
    user_answer = turtle.textinput(title="India states", prompt="what's the another state name: ").title()
    if user_answer == "Exit":
        missing_states = []
        for state in data_list:
            if state not in guesses:
                missing_states.append(state)
        remain_data = pandas.DataFrame(missing_states)
        remain_data.to_csv("missed_india_states.csv")
        break
    if user_answer in data_list:
        guesses.append(user_answer)
        tur = turtle.Turtle()
        tur.penup()
        tur.hideturtle()
        states_cor = data[data.States == user_answer]
        tur.goto(int(states_cor.x), int(states_cor.y))
        tur.write(user_answer)




# def get_coor_on_click(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(get_coor_on_click)
# #screen.mainloop()

#screen.exitonclick()
