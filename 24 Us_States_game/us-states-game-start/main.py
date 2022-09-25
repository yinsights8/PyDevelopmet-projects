import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"  # "This is a path to reach my image"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# print(data[data.state == "Ohio"])
# print(data.x)
data_list = data.state.to_list()
guesses = []

while len(guesses) < 50:
    user_answer = turtle.textinput(title=f"{len(guesses)}/50 States Correct",
                                   prompt="What's the another state name ?").title()

    if user_answer == "Exit":
        missing_states = [state for state in data_list if state not in guesses]
        # missing_states = []
        # for state in data_list:
        #     if state not in guesses:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # check if the user_answer in the data_list
    if user_answer in data_list:
        guesses.append(user_answer)
        # if the name is in the list then send this name to their coordinates
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # print(data[data["state"] == "Ohio"])
        states_data = data[data.state == user_answer]
        t.goto(int(states_data.x), int(states_data.y))
        t.write(user_answer)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()  # the use of this command is even if we click on screen, the screen will never going to end the
# task
